from django.contrib import admin
from django.db.models import Sum
from django.db.models import F

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

    # Contact for Invoice
    def contact_name(self, obj):
        addressId = Address.objects.filter(invoice=obj.id)[:1]
        contactObj = Contact.objects.filter(address=addressId)
        return contactObj[0].name

    # All amount for InvoicePosition 
    def total_amount(self, obj):
        # Only get value as float without tags
        amount = InvoicePosition.objects.filter(invoice=obj.id).aggregate(sum=Sum(F('amount') * F('quantity')))['sum']
        isString = isinstance(amount, str)
        if isString == True:
            #format an two decimal digits
            amount = '{:0.2f}'.format(amount)
        return amount