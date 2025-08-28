from django.db import models
from users.models import User

class Appointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_appointments')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment with {self.teacher.username} on {self.appointment_date}"
