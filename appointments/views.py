from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import Appointment
from .serializers import AppointmentSerializer
from scheduling.models import TimeSlot

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['patch'], url_path='reschedule')
    def reschedule(self, request, pk=None):
        appointment = self.get_object()
        new_timeslot_id = request.data.get('timeslot')
        if new_timeslot_id:
            appointment.timeslot_id = new_timeslot_id
            appointment.save()
            return Response({'message': 'Rescheduled successfully'})
        return Response({'error': 'Missing timeslot'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='cancel')
    def cancel(self, request, pk=None):
        appointment = self.get_object()
        appointment.status = 'cancelled'
        appointment.save()
        return Response({'message': 'Cancelled successfully'})

# Dynamic pricing endpoint
@api_view(['GET'])
def pricing_quote(request):
    doctor_id = request.GET.get('doctor')
    slot_id = request.GET.get('slot')
    slot = TimeSlot.objects.get(id=slot_id)
    base_price = 100  # simple flat fee
    multiplier = 1.2 if slot.start_time.hour in range(9, 17) else 1.0
    return Response({"price": base_price * multiplier})
