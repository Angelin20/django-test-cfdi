# Generated by Django 5.1.7 on 2025-03-20 23:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tax_regime',
            field=models.CharField(default='601', max_length=5, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(3)]),
        ),
    ]
