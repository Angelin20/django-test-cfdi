from django.contrib import admin
from .models import branch,company,current_version,cfdi_provider

admin.site.register([current_version,company,branch,cfdi_provider])
