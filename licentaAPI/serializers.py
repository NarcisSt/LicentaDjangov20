from rest_framework import serializers
from .models import Teams, Players


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('name', 'country', 'city', 'points')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ('first_name', 'last_name', 'shirt_number', 'position', 'age', 'team')
