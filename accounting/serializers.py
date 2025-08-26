from rest_framework import serializers
from .models import ExpiringToken
from django.contrib.auth import get_user_model

User = get_user_model()

class TokenCreateSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("EJA-00001:User does not exist")
        return value
