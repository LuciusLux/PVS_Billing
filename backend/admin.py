from django.contrib import admin

# Register your models here.
from .models import Contact, Country, Address, Invoice, InvoicePosition

@admin.register(Contact)
class ContactAdmin(admin.ContactAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.CountryAdmin):
    pass

@admin.register(Invoice)
class InvoiceAdmin(admin.InvoiceAdmin):
    pass
