from django.db import models

class TransactionModel(models.Model):
    blockchain = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    # id = models.IntegerField(primary_key=True)
    transaction_type = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)