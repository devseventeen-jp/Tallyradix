from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUser
from .models import ExpiringToken
from .serializers import TokenCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminTokenCreateView(generics.GenericAPIView):
    serializer_class = TokenCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        user = User.objects.get(username=username)

        # Re-create token
        ExpiringToken.objects.filter(user=user).delete()
        token = ExpiringToken.objects.create(user=user)

        return Response({"username": user.username, "token": token.key}, status=status.HTTP_201_CREATED)
