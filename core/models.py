from django.db import models

class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    schedule = models.TextField()  # Changed 'hours' to 'schedule' and made it a TextField

    def __str__(self):
        return self.name
