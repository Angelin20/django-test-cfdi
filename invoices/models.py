from django.db import models
from products.models import Product
from customers.models import Customer

class Invoice(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Invoice number")
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True,verbose_name="Customer")
    date_sale = models.DateField(verbose_name="Date of sale")
    total = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total")
    total_taxes = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total & Taxes")
    state = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('canceled', 'Canceled')
        ],
        default='pending',
        verbose_name="State"
    )
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Update date")
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
        ordering = ['-date_sale']

    def __str__(self):
        return f"Invoice {self.id} - {self.id_customer}"
    
class Invoicedetail(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Invoice detail identifier")
    id_invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,blank=True,null=True,verbose_name="Invoice number")
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True,verbose_name="Product identifier")
    quantity = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Quantity",default=1)
    total = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total")
    total_taxes = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total & Taxes")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Update date")
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Invoice detail"
        verbose_name_plural = "Invoice details"
        ordering = ['-id_invoice']

    def __str__(self):
        return f"Invoice {self.id_invoice} - {self.id_product}"