from rest_framework.urls import path
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet

router = DefaultRouter()

router.register(r"", PaymentViewSet, basename="payments")

urlpatterns = router.urls
