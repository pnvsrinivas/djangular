import ldap

from django.contrib.auth.models import User
from rest_framework import views, status
from rest_framework.response import Response
from apis.modules.auth.serializers import AuthSerializer
from apis.core.ldap import authenticate
from apis.core.utils import get_object_or_None
from rest_framework.permissions import AllowAny
from apis.core.exceptions import InvalidCredentialsException

import logging
logger = logging.getLogger('apis.logger')

class AuthViewSet(views.APIView):

    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        username = request.POST.get('username')
        password = request.POST.get('password')
        logger.info("Logging...")
        is_valid, message = authenticate(username, password)
        if is_valid:
            user, _ = User.objects.get_or_create(username=username)
            serializer = AuthSerializer(user, context={ 'request': request })
            return Response(serializer.data)
        
        raise InvalidCredentialsException(detail=message)