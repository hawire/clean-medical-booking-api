from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from appointments.models import Appointment
from notifications.models import Notification
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class Command(BaseCommand):
    help = "Seed demo users, appointments, and notifications"

    def handle(self, *args, **kwargs):
        # Admin
        admin, _ = User.objects.get_or_create(username="admin", defaults={
            "email": "admin@example.com", "role": "admin", "is_staff": True, "is_superuser": True
        })
        admin.set_password("admin123")
        admin.save()

        # Doctors
        doctors = []
        for i in range(1, 4):
            u, _ = User.objects.get_or_create(username=f"dr_{i}", defaults={
                "email": f"dr_{i}@example.com", "role": "doctor"
            })
            u.set_password("test123")
            u.save()
            doctors.append(u)

        # Patients
        patients = []
        for i in range(1, 6):
            u, _ = User.objects.get_or_create(username=f"patient_{i}", defaults={
                "email": f"patient_{i}@example.com", "role": "patient"
            })
            u.set_password("test123")
            u.save()
            patients.append(u)

        # Appointments + Notifications
        now = timezone.now()
        for i, p in enumerate(patients):
            d = doctors[i % len(doctors)]
            appt, _ = Appointment.objects.get_or_create(
                title=f"Checkup {i+1}",
                patient=p,
                doctor=d,
                scheduled_at=now + timedelta(days=i+1),
                defaults={"description": "Routine checkup"}
            )
            Notification.objects.get_or_create(
                user=p,
                type="appointment_reminder",
                message=f"Reminder: {appt.title} with {d.username} on {appt.scheduled_at:%Y-%m-%d %H:%M}"
            )

        self.stdout.write(self.style.SUCCESS("Seeded admin, doctors, patients, appointments, notifications."))
