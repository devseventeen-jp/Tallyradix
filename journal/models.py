from django.db import models

class Account(models.Model):
    """Account Title Master"""
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.code} {self.name}"


class JournalEntry(models.Model):
    """Journal voucher (header part)"""
    date = models.DateField()
    description = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return f"{self.date} {self.description}"


class JournalEntryLine(models.Model):
    """Transaction details (debit and credit for each line)"""
    entry = models.ForeignKey(JournalEntry, related_name="lines", on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    credit = models.DecimalField(max_digits=15, decimal_places=3, default=0)

    def __str__(self):
        return f"{self.account.name} D:{self.debit} C:{self.credit}"
