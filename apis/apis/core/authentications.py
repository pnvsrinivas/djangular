from django.contrib.auth.models import User
from rest_framework import exceptions, authentication

class LdapAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header:
            token_type, token = auth_header.split(' ')
            try:
                username = token
                user = User.objects.get(username=username)
                request.user = user
            except :
                raise exceptions.AuthenticationFailed(('User not found!!'))
            return (user , None)

        return None