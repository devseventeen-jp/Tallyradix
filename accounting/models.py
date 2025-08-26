from django.conf import settings
from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token
from datetime import timedelta

class ExpiringToken(Token):
    """ DRF Token  with expiration date """
    created = models.DateTimeField(auto_now_add=True)

    @property
    def is_expired(self):
        expire_time = self.created + timedelta(days=getattr(settings, "TOKEN_EXPIRE_DAYS", 30))
        return timezone.now() > expire_time
