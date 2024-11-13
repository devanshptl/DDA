from django.urls import path
from .views import InvoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = router.urls
