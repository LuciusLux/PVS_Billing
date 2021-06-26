from django.contrib import admin

# Register your models here.
from .models import Contact, Country, Address, Invoice, InvoicePosition

# Inline for the models here.
class ContactInline(admin.StackedInline):
    model = Address
    extra = 0

class InvoiceInline(admin.StackedInline):
    model = InvoicePosition
    extra = 0

# Register Contact (Inline, filter, search, list).
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_filter = ['type']
    search_fields = ['name']
    list_display = ['__str__', 'type', 'count_address']

# Register Country (search).
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['value', 'key']

# Register Invoice (Inline, search, list).
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceInline]
    search_fields = ['address__contact__name','title']
    list_display = ['contact_name','date', 'due', 'total_amount']