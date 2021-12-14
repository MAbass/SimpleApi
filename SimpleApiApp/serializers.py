from rest_framework import serializers

from SimpleApiApp.models import Hero


class HeroSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    alias = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Hero.objects.create(**validated_data)

    class Meta:
        model = Hero
        fields = '__all__'
