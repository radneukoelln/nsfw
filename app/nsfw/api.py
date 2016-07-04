from .models import Alert, Station, Report, Subscription, Email
from rest_framework import serializers, viewsets


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'kind', 'date')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station


class AlertSerializer(serializers.ModelSerializer):
    report = ReportSerializer()
    station = StationSerializer()

    class Meta:
        model = Alert


class SubscriptionSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='email.email', read_only=False)

    class Meta:
        fields = ('email', 'station')
        model = Subscription

    def create(self, validated_data):
        email, created = Email.objects.get_or_create(email=validated_data.pop('email')['email'])
        station = validated_data.pop('station')
        sub, created = Subscription.objects.get_or_create(email=email, station=station)
        return sub


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    def get_queryset(self):
        id_value = self.request.query_params.get('station', None)
        if id_value:
            id_list = id_value.split(',')
            queryset = Alert.objects.filter(station__in=id_list)
            return queryset
        else:
            return Alert.objects.all()
