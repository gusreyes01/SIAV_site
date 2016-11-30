from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Suscripcion(models.Model):
    email_suscripcion = models.CharField(null=True, blank=True, max_length=255)
    