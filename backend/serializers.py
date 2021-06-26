from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Contact, Address, Invoice, InvoicePosition, Country

# Create Nested and Read Only for Address.
class AddressNestedSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'zip', 'city']
        read_only_fields = ['id', 'street', 'zip', 'city']

# Create Nested and Read Only for Invoice.
class InvoicePositionNestedSerializer(ModelSerializer):
    total = serializers.FloatField(source='total')

    class Meta:
        model = InvoicePosition
        fields = ['id', 'title', 'amount', 'quantity', 'total']
        ReadOnlyField = ['id', 'title', 'amount', 'quantity', 'total']

class ContactSerializer(ModelSerializer):
    Address = AddressNestedSerializer(many=True, read_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'name', 'type', 'email', 'salutation', 'address']
        read_only_fields = ['address']

class ContactCreateSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerializer(ModelSerializer):
    country_name = serializers.CharField(source='country')
    contact = serializers.CharField()

    class Meta:
        model = Address
        fields = ['id', 'street', 'zip', 'city', 'country_name', 'contact']

class AddressCreateSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class InvoiceSerializer(ModelSerializer):
    positions = InvoicePositionNestedSerializer(many=True, read_only=True)
    contact_name = serializers.CharField(source='contactName')
    total_amount = serializers.FloatField(source='totalAmount')

    class Meta:
        model = Invoice
        fields = ['id', 'title', 'body', 'date', 'due', 'condition', 'address', 'positions', 'contact_name', 'total_amount',]
        ReadOnlyField = ['positions', 'contact_name', 'total_amount',]

class InvoiceCreateSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoicePositionSerializer(ModelSerializer):
    class Meta:
        model = InvoicePosition
        fields = ['id', 'title', 'body', 'amount', 'quantity', 'invoice']

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['key', 'value']
    

