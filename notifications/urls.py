from django.urls import path
from .views import test_notification

urlpatterns = [
    path('test/', test_notification, name='test_notification'),
]
