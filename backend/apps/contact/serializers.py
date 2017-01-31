from rest_framework import serializers
from models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.message = validated_data.get('message', instance.message)

        instance.save()
        return instance
