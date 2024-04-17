from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = models.IntegerField(null=True, default=0, blank=False)
    email = models.EmailField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    type = models.CharField(max_length=64, null=False, blank=False)
