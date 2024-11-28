from rest_framework import serializers
from .models import Cat, Mission, Target
import requests

THE_CAT_API_URL='https://api.thecatapi.com/v1/breeds'

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

    def validate_breed(self, value):
        # Validate breed with TheCatAPI
        url = THE_CAT_API_URL
        response = requests.get(url)
        breeds = [breed['name'].lower() for breed in response.json()]
        if value.lower() not in breeds:
            raise serializers.ValidationError("Invalid breed.")
        return value

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id','name', 'country', 'notes', 'complete']

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'complete', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets')
        instance.complete = validated_data.get('complete', instance.complete)
        instance.save()
        
        for target_data in targets_data:
            target, created = Target.objects.update_or_create(mission=instance, name=target_data['name'], defaults=target_data)
        
        return instance
