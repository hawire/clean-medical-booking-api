from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from appointments.models import Appointment
from scheduling.models import TimeSlot
from waitlist.models import WaitlistEntry

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def overview(request):
    total_bookings = Appointment.objects.count()
    cancellations = Appointment.objects.filter(status='cancelled').count()
    slots_total = TimeSlot.objects.count()
    slots_filled = Appointment.objects.exclude(status='cancelled').count()
    utilization = (slots_filled / slots_total) * 100 if slots_total else 0
    waitlist_total = WaitlistEntry.objects.count()
    waitlist_fulfilled = WaitlistEntry.objects.filter(status='fulfilled').count()

    return Response({
        "total_bookings": total_bookings,
        "cancellations": cancellations,
        "utilization_rate": utilization,
        "waitlist_total": waitlist_total,
        "waitlist_fulfilled": waitlist_fulfilled,
    })
