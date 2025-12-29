from scheduling.models import TimeSlot
from users.models import User
from datetime import datetime

def suggest_slots(patient, specialty=None, urgency="routine"):
    now = datetime.now()
    slots = TimeSlot.objects.filter(start_time__gte=now, is_available=True)

    scored = []
    for slot in slots:
        score = 0
        if urgency == "urgent":
            score += 10
        if specialty and specialty in [s.name for s in slot.doctor.specialties.all()]:
            score += 5
        if patient.no_show_rate > 0.3:
            score -= 2
        if slot.start_time.hour in range(9, 17):  # peak hours
            score += 3
        scored.append((score, slot))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [s for _, s in scored[:5]]  # top 5 slots
