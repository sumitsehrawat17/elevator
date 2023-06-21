from rest_framework import serializers
from .models import ElevatorSystem,Elevator,Request


class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystem
        fields = '__all__'
class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'
class RequestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    floor = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    is_complete = serializers.BooleanField(read_only=True)
    class Meta:
        model = Request
        fields = ['floor','name','created_at',"is_complete"]

    def create(self,validated_data):
        validated_data.pop('name')
        return super().create(validated_data)