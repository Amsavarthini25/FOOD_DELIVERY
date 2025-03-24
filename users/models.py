from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    address = models.TextField()
    contact = models.CharField(max_length=20, unique=True)
    payment_details = models.TextField()
    special_instructions = models.TextField(blank=True, null=True)  # Stores allergies, preferences

    def __str__(self):
        return self.username
