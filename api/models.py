from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class FormModel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    type = models.ForeignKey(to='RequestType', on_delete=models.CASCADE, max_length=32, null=False, blank=False)

class RequestType(models.Model):
    type = models.CharField(primary_key=True, max_length=32)
    amount = models.IntegerField(default=0)
