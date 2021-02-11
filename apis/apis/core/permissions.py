from rest_framework import permissions
from django.contrib.auth.models import User

class HasPermission(permissions.BasePermission):
    def has_permission(self, request , view):
        return request.user.is_authenticated