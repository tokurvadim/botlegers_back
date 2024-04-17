from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class FormModel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    type = models.CharField(max_length=64, null=False, blank=False)
