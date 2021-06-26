from django.db import models
from django.db.models import Sum
from django.db.models import F

CONTACT_TYPE_CHOICES = (
    ('private', 'Privat'),
    ('company', 'Company'),
)

# Create model Contact (type(Text20, selectlist), name(Text256), email(Text256, email valid), salutation(Text256)).
class Contact(models.Model):
    type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    salutation = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    @property
    def count_address(self):
        """
        Return count address of current instance
        """
        return self.address.select_related().count()

# Create model Country (key(Text20), value(Text256)).
class Country(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.CharField(max_length=256)

    def __str__(self):
        return self.value

# Create model Address (street(Text256), zip(Text10), city(Text256)).
class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='address')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return self.street + ", " + self.zip + " " + self.city

# Create model Invoice (title(Text256), body(longtext), date(datum), due(datum), condition(Text256)).
class Invoice(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    due = models.DateField(auto_now=False, auto_now_add=False)
    condition = models.CharField(max_length=256, default='10 Tage netto')

    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='invoice')

    def __str__(self):
        return self.title

    #Total Amount for Invoice Serializer
    @property
    def calculateTotalAmount(self):
        totalAmount = InvoicePosition.objects.filter(invoice=self.id).aggregate(sum=Sum(F('amount') * F('quantity')))['sum']
        return totalAmount

    #Total Contact Name for Invoice Serializer
    @property
    def getContactName(self):
        addressId = Address.objects.filter(invoice=self.id)[:1]
        contactObj = Contact.objects.filter(address=addressId)
        return contactObj[0].name    


# Create model InvoicePosition (title(Text256), body(longtext), quantity(number dezi), amount(number dezi)).
class InvoicePosition(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='invoiceposition')

    def __str__(self):
        return self.title

    def calculateTotal(self):
        return self.amount * self.quantity    