# Generated by Django 5.1.7 on 2025-03-20 00:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_key', models.CharField(blank=True, max_length=128)),
                ('company_name', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(13)])),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='company')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='current_version',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('features', models.CharField(blank=True, max_length=120)),
                ('changes', models.TextField(blank=True, max_length=2400)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_key', models.CharField(blank=True, max_length=128)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=40, validators=[django.core.validators.MinLengthValidator(10)])),
                ('email', models.CharField(blank=True, max_length=240)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('conf_ip_ext', models.CharField(blank=True, max_length=40)),
                ('conf_ip_int', models.CharField(blank=True, max_length=40, null=True)),
                ('conf_user', models.CharField(blank=True, max_length=40)),
                ('conf_pass', models.CharField(blank=True, max_length=40)),
                ('conf_db', models.CharField(blank=True, max_length=80)),
                ('conf_port', models.CharField(blank=True, max_length=80, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='branch')),
                ('deleted', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('lat', models.CharField(blank=True, max_length=50, null=True)),
                ('long', models.CharField(blank=True, max_length=50, null=True)),
                ('id_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company')),
            ],
        ),
    ]
