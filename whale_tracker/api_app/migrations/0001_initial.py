# Generated by Django 3.2.9 on 2021-11-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('blockchain', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=200)),
                ('hash', models.CharField(max_length=200)),
            ],
        ),
    ]
