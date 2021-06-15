from django.contrib import admin

# Register your models here.
from .models import Contact, Country, Address, Invoice, InvoicePosition

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass
