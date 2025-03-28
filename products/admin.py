from django.contrib import admin
from .models import Product, category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'date_creation')
    search_fields = ('name', 'description')
    list_filter = [
        'category__name',
        'date_creation',
        'date_update',
        'deleted'
    ]

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_creation')
    search_fields = ('name', 'description')
    list_filter = [
        'branch__name',
        'current_version__name',
        'date_creation',
        'date_update',
        'deleted'
    ]