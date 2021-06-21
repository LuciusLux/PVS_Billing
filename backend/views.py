from django.shortcuts import render
from .serializers import ContactSerializer, ContactCreateSerializer
from .models import Contact,
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ContactApiViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ContactCreateSerializer
        return ContactSerializer