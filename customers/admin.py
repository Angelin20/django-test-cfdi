from django.contrib import admin
from .models import Customer
from .forms import CustomerForm

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','rfc')
    search_fields = ('id','name','phone','email','rfc')
    list_filter = [
        'date_creation',
        'date_update',
        'branch__name',
        'bill_require',
        'country',
        'state',
        'deleted'
    ]
    form = CustomerForm
# Compare this snippet from testcertiffy/customers/views.py: