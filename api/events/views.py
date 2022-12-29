from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    Event,
    Category,
    Comment
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


    @action(methods=['post'], detail=False, description="Endpoint for adding comments")
    def add_comment(self, request, *args, **kwargs):
        content = request.data.get("content", "")
        event = request.data.get("event", 0)
        if content == "" or event == 0:
            return Response({"message": "invalid request"}, status=400)
        event = Event.objects.filter(id=event)
        if not event.exists():
            return Response({"message": "invalid comment id"}, status=400)
        Comment.objects.create(content=content, author=request.user, event__id=event)
        return Response({"message": "ok"})


class CategoryViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
