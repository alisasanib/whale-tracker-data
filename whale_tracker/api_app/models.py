from django.db import models

class TransactionModel(models.Model):
    blockchain = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    # id = models.IntegerField(primary_key=True)
    transaction_type = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)
    from_source = models.JSONField(encoder=None, decoder=None, default=list)
    to_source = models.JSONField(encoder=None, decoder=None, default=list)
    timestamp = models.PositiveBigIntegerField(default=0)
    amount = models.BigIntegerField(default=0)
    amount_usd = models.BigIntegerField(default=0)
    transaction_count = models.SmallIntegerField(default=0)