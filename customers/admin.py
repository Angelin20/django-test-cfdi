from django.contrib import admin
from .models import Customer
from .forms import CustomerForm

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','rfc')
    search_fields = ('id','name','phone','email','rfc')
    form = CustomerForm
# Compare this snippet from testcertiffy/customers/views.py: