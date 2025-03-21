from django.contrib import admin
from .models import Product, category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'date_creation')
    search_fields = ('name', 'description')

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_creation')
    search_fields = ('name', 'description')