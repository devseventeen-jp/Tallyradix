from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from accounts.authentication import ExpiringTokenAuthentication

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all().order_by("-date")
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [ExpiringTokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        