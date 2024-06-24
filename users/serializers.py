from rest_framework import serializers
from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'chat_id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.chat_id = validated_data.get('chat_id', instance.chat_id)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
