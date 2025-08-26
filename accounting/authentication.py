from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import ExpiringToken

class ExpiringTokenAuthentication(TokenAuthentication):
    model = ExpiringToken

    def authenticate_credentials(self, key):
        token = super().authenticate_credentials(key)
        if token[0].is_expired:
            raise AuthenticationFailed("Token has expired")
        return token
