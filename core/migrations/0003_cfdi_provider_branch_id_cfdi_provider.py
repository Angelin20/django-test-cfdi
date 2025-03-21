# Generated by Django 5.1.7 on 2025-03-21 18:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_branch_options_alter_company_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cfdi_provider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('user', models.CharField(blank=True, max_length=240)),
                ('authorization', models.CharField(blank=True, max_length=240)),
                ('url', models.CharField(blank=True, max_length=240)),
                ('technical_contact', models.CharField(blank=True, max_length=240)),
                ('phone_contact', models.CharField(blank=True, max_length=40, validators=[django.core.validators.MinLengthValidator(10)])),
                ('email_contact', models.CharField(blank=True, max_length=240)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'CFDI Provider',
                'verbose_name_plural': 'CFDI Providers',
                'ordering': ['-date_creation'],
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='id_cfdi_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cfdi_provider'),
        ),
    ]
