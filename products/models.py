from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from core.models import current_version, branch

class category(models.Model):
    id = models.AutoField(primary_key=True)
    id_branch = models.ForeignKey(branch, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500,blank=True)
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=False, auto_now_add=True)
    id_current_version = models.ForeignKey(current_version, on_delete=models.CASCADE,blank=True,null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-date_creation']

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Product identifier")
    name = models.CharField(max_length=100, verbose_name="Name of product")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    stock = models.PositiveIntegerField(verbose_name="Stock")
    category = models.ForeignKey(category, on_delete=models.CASCADE, verbose_name="Category",blank=True,null=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Update date")
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-date_creation']

    def __str__(self):
        return self.name

