from rest_framework import serializers
from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature',]

class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

