# Generated by Django 4.0 on 2022-10-04 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_trade_unique_trades'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='trade',
            name='unique_trades',
        ),
    ]
