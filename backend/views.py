from django.shortcuts import render
from .serializers import ContactSerializer, ContactCreateSerializer, AddressSerializer, AddressCreateSerializer, InvoiceSerializer, InvoiceCreateSerializer, InvoicePositionSerializer, CountrySerializer
from .models import Contact, Address, Invoice, InvoicePosition, Country
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ContactApiViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ContactCreateSerializer
        return ContactSerializer

class AddressApiView(ModelViewSet):
    queryset = Address.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return AddressCreateSerializer
        return AddressSerializer

class InvoiceApiView(ModelViewSet):
    queryset = Invoice.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['address__contact__name']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return InvoiceCreateSerializer
        return InvoiceSerializer

class InvoicePositionApiView(ModelViewSet):
    serializer_class = InvoicePositionSerializer
    queryset = InvoicePosition.objects.all()

class CountryApiView(ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['value']