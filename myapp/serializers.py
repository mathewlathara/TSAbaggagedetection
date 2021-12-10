from rest_framework import serializers

from .models import passenger

class passengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = passenger
        fields = ('id','passenger_name', 'passport_number', 'dept_airport', 'arrive_airport', 'flight_number','url_image')