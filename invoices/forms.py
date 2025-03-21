from django import forms
from .models import Invoice, Invoicedetail

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['id_customer', 'date_sale' ]

class  DetailsForm(forms.ModelForm):
    class Meta:
        model = Invoicedetail
        fields = ['id_product', 'quantity', 'total' ]

