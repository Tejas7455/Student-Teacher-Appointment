from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'teacher':
            return Appointment.objects.filter(teacher=user)
        return Appointment.objects.filter(student=user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

