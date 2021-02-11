from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers define the API representation.
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active', 'date_joined']