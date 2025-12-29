from rest_framework import viewsets, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from .models import TimeSlot, Leave
from .serializers import TimeSlotSerializer, LeaveSerializer
from users.models import User
from datetime import datetime

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='availability')
    def availability(self, request, pk=None):
        doctor = User.objects.get(pk=pk, role='doctor')
        now = datetime.now()
        slots = TimeSlot.objects.filter(doctor=doctor, start_time__gte=now, is_available=True)
        serializer = TimeSlotSerializer(slots, many=True)
        return Response(serializer.data)

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticated]

# Intelligent slot suggestions
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def slot_suggestions(request):
    patient = request.user
    specialty = request.data.get('specialty')
    urgency = request.data.get('urgency', 'routine')

    now = datetime.now()
    slots = TimeSlot.objects.filter(start_time__gte=now, is_available=True)

    scored = []
    for slot in slots:
        score = 0
        if urgency == "urgent":
            score += 10
        if specialty and hasattr(slot.doctor, 'specialties') and specialty in [s.name for s in slot.doctor.specialties.all()]:
            score += 5
        if hasattr(patient, 'no_show_rate') and patient.no_show_rate > 0.3:
            score -= 2
        if slot.start_time.hour in range(9, 17):  # peak hours
            score += 3
        scored.append((score, slot))

    scored.sort(key=lambda x: x[0], reverse=True)
    top_slots = [s for _, s in scored[:5]]

    serializer = TimeSlotSerializer(top_slots, many=True)
    return Response(serializer.data)
