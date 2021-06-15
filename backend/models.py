from django.db import models

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

# Create model Country (key(Text20), value(Text256)).
class Country(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.CharField(max_length=256)

# Create model Address (street(Text256), zip(Text10), city(Text256)).
class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='address')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='address')

# Create model Invoice (title(Text256), body(longtext), date(datum), due(datum), condition(Text256)).
class Invoice(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    due = models.DateField(auto_now=False, auto_now_add=False)
    condition = models.CharField(max_length=256, default='10 Tage netto')

    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='invoice')

# Create model InvoicePosition (title(Text256), body(longtext), quantity(number dezi), amount(number dezi)).
class InvoicePosition(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='invoiceposition')