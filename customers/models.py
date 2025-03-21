from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from core.models import branch
from django.utils.timezone import datetime
import requests
import json

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    id_branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True)
    phone =  models.CharField(max_length=40,blank=True,validators=[MinLengthValidator(10)])
    email = models.CharField(max_length=240,blank=True)
    address = models.CharField(max_length=500,blank=True)
    country = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    zip_code = models.CharField(max_length=20,blank=True)
    bill_require = models.BooleanField(default=False)
    correct_billing_info = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100)
    rfc = models.CharField(max_length=40,validators=[MinLengthValidator(10), MaxLengthValidator(13)])
    tax_regime = models.CharField(max_length=5,validators=[MinLengthValidator(1), MaxLengthValidator(3)],default='601')
    lat = models.CharField(max_length=50,blank=True,null=True)
    long = models.CharField(max_length=50,blank=True,null=True)
    photo = models.ImageField(upload_to='branch',blank=True)
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=False, auto_now_add=True)
    deleted = models.BooleanField(default=False)
        
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['-name']
    
    def save(self, *args, **kwargs):
        pk = self.pk  # pk will be None like objects if self is new instance
        if pk is not None:
            self.date_update = datetime.now()
            if self.bill_require:
                body = json.dumps({
                    "Rfc": self.rfc.upper(),
                    "Name": self.company_name.upper(),
                    "ZipCode": self.zip_code,
                    "FiscalRegime": self.tax_regime
                })
                headers = {
                "User-Agent": "Angelin20",
                "Content-Type": "application/json",
                "Authorization": "",
                "Cookie": ".ASPXAUTH=CF138D33422C94D9D74DC56AAA911486097E6FE16566539348466160A601390CA6978AFF8755284FCF52D599BE751AE6E63BC43006BE5E0D5261F4F310E23E9BAE453933C7E4890A4BB3C29F03CAB04116C9A90A0F8983DE8C75BBD5567C90C8"
                }
                response = requests.request("POST", "https://apisandbox.facturama.mx/customers/validate", headers=headers, data=body)
                if response.status_code == 200:
                    jresponse = response.json()
                    if jresponse["ExistRfc"] == True and jresponse["MatchName"] == True and jresponse["MatchZipCode"] == True and jresponse["MatchFiscalRegime"] == True:
                        self.correct_billing_info = True
                        super().save(*args, **kwargs)
                    else:
                        self.correct_billing_info = False
                        super().save(*args, **kwargs)
                else:
                    raise ValueError(f"Error to verify your Billing data to SAT: {response.text}")
            else:
                self.correct_billing_info = False
                super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    