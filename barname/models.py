from django.db import models
import uuid

class TheUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    clinic_id = models.CharField(max_length=255,null=True)

class TheClinic(models.Model):
    clinic_id = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)
    services = models.CharField(max_length=255,null=True)

class TheAppointments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clinic_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    status = models.CharField(max_length=20)