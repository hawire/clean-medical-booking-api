from django.db import models
from users.models import User

class WaitlistEntry(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'patient'},
        related_name='waitlist_entries_as_patient'   
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'doctor'},
        null=True,
        blank=True,
        related_name='waitlist_entries_as_doctor'    
    )
    desired_date = models.DateField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.patient.username} waiting for {self.doctor.username if self.doctor else 'any doctor'}"
