from rest_framework.serializers import ModelSerializer
from .models import Contact, Address, Invoice, InvoicePosition, Country

# Create Nested and Read Only for Address.
class AddressNestedSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'zip', 'city']
        read_only_fields = ['id', 'street', 'zip', 'city']


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