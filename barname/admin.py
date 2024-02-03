from django.contrib import admin
from .models import TheUser, TheAppointments, TheClinic

admin.site.register(TheUser)
admin.site.register(TheAppointments)
admin.site.register(TheClinic)