from rest_framework import serializers
from .models import JournalEntry, JournalEntryLine, Account

class JournalEntryLineSerializer(serializers.ModelSerializer):
    account_code = serializers.CharField(write_only=True)
    account_name = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = JournalEntryLine
        fields = ["account_code", "account_name", "debit", "credit"]

    def create(self, validated_data):
        code = validated_data.pop("account_code")
        name = validated_data.pop("account_name", "")
        account, _ = Account.objects.get_or_create(code=code, defaults={"name": name})
        return JournalEntryLine.objects.create(account=account, **validated_data)

class JournalEntrySerializer(serializers.ModelSerializer):
    lines = JournalEntryLineSerializer(many=True)
    description = serializers.CharField()

    class Meta:
        model = JournalEntry
        fields = ["id", "transaction_id", "date", "description", "lines", "created_datetime", "created_by"]

    def validate(self, data):
        total_debit = sum(line.get("debit",0) for line in data["lines"])
        total_credit = sum(line.get("credit",0) for line in data["lines"])
        if total_debit != total_credit:
            raise serializers.ValidationError("EJ-00001:The total debit and the total credit do not match.")
        return data

    def create(self, validated_data):
        lines_data = validated_data.pop("lines")
        user = self.context['request'].user 
        entry = JournalEntry.objects.create(created_by=user, **validated_data)
        for line_data in lines_data:
            line_data["entry"] = entry
            JournalEntryLineSerializer().create(line_data)
        return entry
