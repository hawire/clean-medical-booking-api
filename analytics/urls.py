from django.urls import path
from .views import overview

urlpatterns = [
    path('overview/', overview, name='analytics_overview'),
]
