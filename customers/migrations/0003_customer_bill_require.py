# Generated by Django 5.1.7 on 2025-03-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_tax_regime'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bill_require',
            field=models.BooleanField(default=False),
        ),
    ]
