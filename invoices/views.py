from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from uuid import uuid4
from .models import Invoice
from .forms import InvoiceForm


def add(request):
    
    newInvoice = Invoice.objects.create()
    newInvoice.save()
    
    inv = Invoice.objects.get(id=newInvoice[0].id)
    return redirect('create-build-invoice', slug=inv.slug)

    