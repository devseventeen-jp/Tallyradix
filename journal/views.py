from rest_framework import viewsets
from .models import JournalEntry
from .serializers import JournalEntrySerializer

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all().order_by("-date")
    serializer_class = JournalEntrySerializer
