from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, pricing_quote

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('', include(router.urls)),
    path('pricing/quote/', pricing_quote, name='pricing_quote'),
]
