from django.db import models
from django.db.models import F
from phonenumber_field.modelfields import PhoneNumberField


class FormModel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    button = models.CharField(max_length=32, null=False, blank=False)


class ButtonModel(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    amount = models.IntegerField(default=1)

    def update_amount(self, button_name: str):
        button_obj, created = self.objects.get_or_create(name=button_name)
        if not created:
            button_obj.amount = F('amount') + 1
            button_obj.save()
