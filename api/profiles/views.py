from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Profile.objects.all()

    def get_serializer_class(self):
        return ProfileSerializer
