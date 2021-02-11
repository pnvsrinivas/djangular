from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers define the API representation.
class AuthSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        return 'Admin'
        # return 'User'

    def get_token(self, obj):
        return obj.username
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active', 'date_joined', 'token', 'role']