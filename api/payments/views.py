import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from .models import Payment
from .serializers import PaymentSerializer, PaymentCreateSerializer


class PaymentViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.action == "list":
            return Payment.objects.filter(purchaser_email=self.request.GET.get("email", ""), status="SUCCESS")
        return Payment.objects.filter(status="SUCCESS")

    def get_serializer_class(self):
        if self.action == 'create':
            return PaymentCreateSerializer
        return PaymentSerializer
