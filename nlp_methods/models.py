from django.db import models


# Create your models here.
class InputText(models.Model):
    text = models.TextField(blank=False)
    method = models.TextField(blank=True)