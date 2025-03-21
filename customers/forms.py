from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id','id_branch', 'name', 'phone', 'email', 'address', 'country', 'state', 'city', 'zip_code', 'bill_require','correct_billing_info', 'company_name', 'rfc', 'tax_regime', 'lat', 'long', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["correct_billing_info"].disabled = True
        # Or to set READONLY
        self.fields["correct_billing_info"].widget.attrs["readonly"] = True