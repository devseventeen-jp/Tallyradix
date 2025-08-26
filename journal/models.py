import uuid
from django.db import models
from django.conf import settings

class Account(models.Model):
    """Account Title Master"""
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.code} {self.name}"


class JournalEntry(models.Model):
    """Journal voucher (header part)"""
    id = models.BigAutoField(primary_key=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date = models.DateField()
    description = models.CharField(max_length=400, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_id} {self.date} {self.description} {self.created_datetime}"


class JournalEntryLine(models.Model):
    """Transaction details (debit and credit for each line)"""
    entry = models.ForeignKey(JournalEntry, related_name="lines", on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    credit = models.DecimalField(max_digits=15, decimal_places=3, default=0)

    def __str__(self):
        return f"{self.account.name} D:{self.debit} C:{self.credit}"
