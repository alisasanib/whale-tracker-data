from rest_framework import serializers
from .models import TransactionModel


class TransactionSerializer(serializers.ModelSerializer):
    blockchain = serializers.CharField(max_length=200)
    symbol = serializers.CharField(max_length=200)
    transaction_type = serializers.CharField(max_length=200)
    hash = serializers.CharField(max_length=200)
    from_source = serializers.JSONField(encoder=None, decoder=None)
    to_source = serializers.JSONField(encoder=None, decoder=None)
    timestamp = serializers.IntegerField()
    amount = serializers.IntegerField()
    amount_usd = serializers.IntegerField()
    transaction_count = serializers.IntegerField()

    class Meta:
        model = TransactionModel
        fields = ('__all__')
