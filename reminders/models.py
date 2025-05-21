from django.db import models

class Reminder(models.Model):
    REMINDER_TYPE_CHOICES = [
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
    ]

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.message} on {self.date} at {self.time} via {self.reminder_type}"
