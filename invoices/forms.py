from django import forms
from .models import Invoice, Invoicedetail

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer', 'total','total_taxes','date_sale']
        widgets = {
            'total':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
            'total_taxes':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
        }


class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = Invoicedetail
        fields = ['product', 'quantity', 'total', 'total_taxes']
        widgets = {
            'total_taxes':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
        }


