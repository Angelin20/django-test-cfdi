from django import forms
from .models import branch, cfdi_provider, company

class BranchForm(forms.ModelForm):
    class Meta:
        model = branch
        #fields = ['id_branch', 'name', 'phone', 'email', 'address', 'country', 'state', 'city', 'zip_code', 'bill_require','correct_billing_info', 'company_name', 'rfc', 'tax_regime', 'lat', 'long', 'photo']

class Cfdi_providerForm(forms.ModelForm):
    class Meta:
        model = cfdi_provider
        #fields = ['id','id_branch', 'name', 'phone', 'email', 'address', 'country', 'state', 'city', 'zip_code', 'bill_require','correct_billing_info', 'company_name', 'rfc', 'tax_regime', 'lat', 'long', 'photo']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        #fields = ['id','id_branch', 'name', 'phone', 'email', 'address', 'country', 'state', 'city', 'zip_code', 'bill_require','correct_billing_info', 'company_name', 'rfc', 'tax_regime', 'lat', 'long', 'photo']
