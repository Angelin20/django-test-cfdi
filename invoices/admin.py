from django.contrib import admin
from .models import Invoice, Invoicedetail
from .forms import InvoiceForm


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_customer', 'total','state','date_sale')
    search_fields = ('id', 'customer','date_sale','state')
    form = InvoiceForm

@admin.register(Invoicedetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_invoice', 'id_product','total','quantity','total_taxes')
    search_fields = ('id', 'id_invoice','id_product')