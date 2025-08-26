import uuid
from django.db import models
from django.conf import settings
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

AES_KEY = os.getenv("AES_KEY").encode()

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
#    description = models.CharField(max_length=400, blank=True)
    description_encrypted = models.BinaryField(blank=True, null=True)

    created_datetime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def description(self):
        if self.description_encrypted:
            cipher = AES.new(AES_KEY, AES.MODE_CBC, iv=self.description_encrypted[:16])
            decrypted = unpad(cipher.decrypt(self.description_encrypted[16:]), AES.block_size)
            return decrypted.decode()
        return None

    @description.setter
    def description(self, value):
        iv = os.urandom(16)
        cipher = AES.new(AES_KEY, AES.MODE_CBC, iv=iv)
        encrypted = iv + cipher.encrypt(pad(value.encode(), AES.block_size))
        self.description_encrypted = encrypted

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
