from rest_framework import serializers
from models import Pricing, Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.company = validated_data.get('company', instance.company)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.request = validated_data.get('request', instance.request)

        instance.save()
        return instance

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request