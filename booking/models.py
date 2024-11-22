from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Free Trial", "Free Trial"),
    )
TIME_CHOICES = (
    ("7 AM", "7 AM"),
    ("8 AM", "8 AM"),
    ("9 AM", "9 AM"),
    ("1 PM", "1 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("6 PM", "6 PM"),
    ("7:30 PM", "7:30 PM"),
)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Free Trial")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="7 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
