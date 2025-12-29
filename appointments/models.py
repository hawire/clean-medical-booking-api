from django.db import models
from users.models import User
from scheduling.models import TimeSlot

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='appointments',
        limit_choices_to={'role': 'patient'}
    )
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='appointments_as_doctor',
        limit_choices_to={'role': 'doctor'}
    )
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} with {self.doctor.username} at {self.timeslot.start_time}"
