from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer



