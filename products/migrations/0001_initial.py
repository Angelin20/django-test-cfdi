# Generated by Django 5.1.7 on 2025-03-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of product')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('stock', models.PositiveIntegerField(verbose_name='Stock')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-date_creation'],
            },
        ),
    ]
