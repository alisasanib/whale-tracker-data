from rest_framework import serializers
from .models import TransactionModel


class TransactionSerializer(serializers.ModelSerializer):
    blockchain = serializers.CharField(max_length=200)
    symbol = serializers.CharField(max_length=200)
    transaction_type = serializers.CharField(max_length=200)
    hash = serializers.CharField(max_length=200)
    # id = serializers.IntegerField(primary_key=True)

    class Meta:
        model = TransactionModel
        fields = ('__all__')
