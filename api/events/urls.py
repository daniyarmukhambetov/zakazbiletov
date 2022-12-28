from rest_framework.urls import path
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, CategoryViewSet

router = DefaultRouter()
router.register("events", EventViewSet, basename="events")
router.register("categories", CategoryViewSet, basename="categories")
urlpatterns = router.urls
