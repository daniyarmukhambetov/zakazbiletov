from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import (
    Event,
    Category
)
from .serializers import (
    EventSerializer,
    EventListSerializer,
    CategorySerializer
)


# Create your views here.
class EventViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        "begins_date",
        "category_id",
        "city",
    ]
    search_fields = [
        "name",
    ]
    ordering_fields = [
        "begins_time",
        "begins_date"
    ]

    def get_queryset(self):
        return Event.objects.filter()

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        if self.action == 'retrieve':
            return EventSerializer


class CategoryViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
