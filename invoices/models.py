from django.db import models
from products.models import Product
from customers.models import Customer
from django.db.models import UniqueConstraint
from django.utils.timezone import datetime
import requests
import json

class Invoice(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Invoice number")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True,verbose_name="Customer")
    date_sale = models.DateField(verbose_name="Date of sale")
    total = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total of invoice")
    total_taxes = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total of invoice & Taxes")
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

    def save(self, *args, **kwargs):
        pk = self.pk  # pk will be None like objects if self is new instance
        if pk is not None:
            self.date_update = datetime.now()
            if self.customer.bill_require:
                body = json.dumps({
                    "Rfc": self.customer.rfc.upper(),
                    "Name": self.customer.company_name.upper(),
                    "ZipCode": self.customer.zip_code,
                    "FiscalRegime": self.customer.tax_regime
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
                        
                        #Inicio de factura
                        url = "https://apisandbox.facturama.mx/3/cfdis"

                        payload = json.dumps({
                        "NameId": "34",
                        "Folio": "100",
                        "Serie": None,
                        "CfdiType": "I",
                        "Currency": "MXN",
                        "PaymentForm": "01",
                        "PaymentMethod": "PUE",
                        "OrderNumber": self.pk,
                        "ExpeditionPlace": "78000",
                        "Date": "2025-03-27T12:00:00",
                        "PaymentConditions": "",
                        "Observations": "Elemento Observaciones solo visible en PDF",
                        "Exportation": "01",
                        "GlobalInformation": {
                            "Periodicity": "04",
                            "Months": "03",
                            "Year": "2025"
                        },
                        "Receiver": {
                            "Rfc": "XAXX010101000",
                            "Name": "PUBLICO EN GENERAL",
                            "CfdiUse": "S01",
                            "TaxZipCode": "78000",
                            "FiscalRegime": "616"
                        },
                        "Items": [
                            {
                            "ProductCode": "10101504",
                            "IdentificationNumber": "EDL",
                            "Description": "Estudios de laboratorio",
                            "Unit": "NO APLICA",
                            "UnitCode": "MTS",
                            "UnitPrice": 50,
                            "Quantity": 2,
                            "Subtotal": 100,
                            "TaxObject": "02",
                            "Taxes": [
                                {
                                "Total": 16,
                                "Name": "IVA",
                                "Base": 100,
                                "Rate": 0.16,
                                "IsRetention": False
                                }
                            ],
                            "Total": 116
                            }
                        ]
                        })
                        headers = {
                        'Content-Type': 'application/json',
                        'User-Agent': 'Angelin20',
                        'Authorization': "",
                        'Cookie': '.ASPXAUTH=2C124EAAC4E643D4F18F579A5F6B932D9AA78871D16FC9169B39A6620E69C049EDB0A3FC227E0BF2C3B329C351668316344A77C84DD2928C70A202C188A76D06C316FFEA2F554E8166126A334E678C36A1933C4E65A0730035EAE9B66B41AD6D'
                        }

                        response = requests.request("POST", url, headers=headers, data=payload)
                        #fin de factura
                        super().save(*args, **kwargs)
                    else:
                        raise ValueError(f"Error to verify your Billing data to SAT for: {self.customer.company_name} - {self.customer.rfc} ")
                else:
                    raise ValueError(f"Error to verify your Billing data to SAT: {response.text}")
            else:
                super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer}"
    
class Invoicedetail(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Invoice detail identifier")
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,blank=True,null=True,verbose_name="Invoice number")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True,verbose_name="Product identifier")
    quantity = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Quantity",default=1)
    total = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total of product price")
    total_taxes = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total of product & Taxes")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Update date")
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Invoice detail"
        verbose_name_plural = "Invoice details"
        ordering = ['-invoice']
        constraints = [
            UniqueConstraint(fields=['invoice', 'product','deleted'], name='unique_host_migration'),
        ]
        
    def __str__(self):
        return f"Invoice {self.invoice} - {self.product}"