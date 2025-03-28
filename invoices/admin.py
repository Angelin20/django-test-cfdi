from django.contrib import admin
from .models import Invoice, Invoicedetail
from .forms import InvoiceForm, InvoiceDetailForm

class InvoiceDetailInline(admin.StackedInline):
    model = Invoicedetail
    fields = ['product', 'quantity', 'total', 'total_taxes']
    form = InvoiceDetailForm
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailInline]
    list_display = ('customer', 'total','total_taxes','date_sale', 'get_detail_product')
    fields = ['customer', 'total','total_taxes','date_sale']
    search_fields = ('customer__name', )
    list_filter = [
        'customer__name',
        'state',
        'date_sale',
        'total'
    ]
    form = InvoiceForm
    class Media:
        js = (
            'js/admin.js',   # inside app static folder
        )
    

    def get_detail_product(self, obj):
        qs = Invoicedetail.objects.filter(invoice=obj.id).values_list('product__name', 'quantity', 'total',)
        ret = []
        for q in qs:
            q = list(q)
            ret.append(q[0] + ' ( Qty:' + str(q[1]) + ' - Tot:$' + str(q[2]) +')')
        return ret
    get_detail_product.short_description = 'Product(s)'

class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('invoice','invoice__customer__name','invoice__total','invoice__state','invoice__date_sale', 'product__name','total','quantity','total_taxes')
    search_fields = ('invoice__customer__name','product__name','invoice__state','invoice__date_sale','invoice__total','total','quantity','total_taxes')
    list_filter = [
        'invoice__customer__name',
        'product__name',
        'invoice__state',
        'invoice__date_sale',
        'invoice__total',
        'total',
        'quantity',
        'total_taxes'
    ]

admin.site.register(Invoice, InvoiceAdmin)