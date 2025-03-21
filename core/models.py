from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Models for general use into app
class current_version(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=120,blank=True)
    features = models.CharField(max_length=120,blank=True)
    changes = models.TextField(max_length=2400,blank=True)
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=False, auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versions"
        ordering = ['-date_creation']

    def __str__(self):
        return self.name

class cfdi_provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True)
    user = models.CharField(max_length=240,blank=True)
    authorization = models.CharField(max_length=240,blank=True)
    url = models.CharField(max_length=240,blank=True)
    technical_contact = models.CharField(max_length=240,blank=True)
    phone_contact =  models.CharField(max_length=40,blank=True,validators=[MinLengthValidator(10)])
    email_contact = models.CharField(max_length=240,blank=True)
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=False, auto_now_add=True)
    deleted = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "CFDI Provider"
        verbose_name_plural = "CFDI Providers"
        ordering = ['-date_creation']

    def __str__(self):
        return self.name

class company(models.Model):
    id = models.AutoField(primary_key=True)
    company_key = models.CharField(max_length=128,blank=True)
    company_name = models.CharField(max_length=100)
    rfc = models.CharField(max_length=40,validators=[MinLengthValidator(10), MaxLengthValidator(13)])
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='company',blank=True)
    id_current_version = models.ForeignKey(current_version, on_delete=models.CASCADE,blank=True,null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['-date_creation']

    def __str__(self):
        return self.company_key

class branch(models.Model):
    id = models.AutoField(primary_key=True)
    id_company = models.ForeignKey(company, on_delete=models.CASCADE)
    id_cfdi_provider = models.ForeignKey(cfdi_provider, on_delete=models.CASCADE,blank=True,null=True)
    branch_key = models.CharField(max_length=128,blank=True)
    name = models.CharField(max_length=100,blank=True)
    phone =  models.CharField(max_length=40,blank=True,validators=[MinLengthValidator(10)])
    email = models.CharField(max_length=240,blank=True)
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=False, auto_now_add=True)
    conf_ip_ext =  models.CharField(max_length=40,blank=True)
    conf_ip_int =  models.CharField(max_length=40,blank=True,null=True)
    conf_user =  models.CharField(max_length=40,blank=True)
    conf_pass =  models.CharField(max_length=40,blank=True)
    conf_db =  models.CharField(max_length=80,blank=True)
    conf_port =  models.CharField(max_length=80,blank=True,null=True)
    photo = models.ImageField(upload_to='branch',blank=True)
    deleted = models.BooleanField(default=False)
    address = models.CharField(max_length=500,blank=True)
    lat = models.CharField(max_length=50,blank=True,null=True)
    long = models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
        ordering = ['-date_creation']

    def __str__(self):
        return self.branch_key
    