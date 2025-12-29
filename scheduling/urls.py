from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimeSlotViewSet, LeaveViewSet, slot_suggestions

router = DefaultRouter()
router.register(r'timeslots', TimeSlotViewSet, basename='timeslot')
router.register(r'leaves', LeaveViewSet, basename='leave')

urlpatterns = [
    path('', include(router.urls)),
    path('suggestions/slots/', slot_suggestions, name='slot_suggestions'),
]
