from django.contrib import admin
from .models import branch,company,current_version,cfdi_provider


@admin.register(current_version)
class CurrentVersionAdmin(admin.ModelAdmin):
    list_display = ('name','features','changes','date_creation','date_update')
    search_fields = ('name','features','changes','date_creation','date_update')
    list_filter = [
        'date_creation',
        'date_update',
        'deleted'
    ]

@admin.register(cfdi_provider)
class CfdiProviderAdmin(admin.ModelAdmin):
    list_display = ('name','user','url','technical_contact','phone_contact','email_contact','date_creation','date_update')
    search_fields = ('name','user','url','technical_contact','phone_contact','email_contact','date_creation','date_update')
    list_filter = [
        'date_creation',
        'date_update',
        'deleted'
    ]

@admin.register(company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code','name','rfc','date_creation','date_update','photo','current_version')
    search_fields = ('code','name','rfc')
    list_filter = [
        'current_version',
        'date_creation',
        'date_update',
        'deleted'
    ]

@admin.register(branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('code','name','phone','email','company__name','cfdi_provider__name','deleted')
    search_fields = ('code','name','phone','email','company__name','cfdi_provider__name')
    list_filter = [
        'company__name',
        'cfdi_provider__name',
        'deleted'
    ]