from django.db import models
from django.db.models import F
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class FormModel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)



class BriefModel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(null=False, blank=False)
    social = models.CharField(null=False, blank=False)
    button = models.CharField(max_length=32, null=False, blank=False, default='')
    budget = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    deadline = models.CharField(max_length=32, null=False, blank=False)
    technologies = models.CharField(null=True, blank=True)
    srs_link = models.URLField(null=True, blank=True)
    design_link = models.URLField(null=True, blank=True)
    portfolio = models.CharField(null=True, blank=True)
    message = models.TextField(null=False, blank=False)



class AboutUsModel(models.Model):
    title = models.CharField(null=False, blank=False)
    button = models.CharField(max_length=32)
    technologies = models.JSONField()
    description = models.TextField()
    questions = models.JSONField()
    advantages = models.TextField()



class PortfolioModel(models.Model):
    title = models.TextField(null=False, blank=False)
    button = models.CharField(max_length=32)
    description = models.CharField(null=False, blank=False)
    done = models.JSONField()
    feature = models.CharField(null=False, blank=False)
    technologies = models.JSONField()



class ButtonModel(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    amount = models.IntegerField(default=1)

    def update_amount(self, button_name: str):
        button_obj, created = self.objects.get_or_create(name=button_name)
        if not created:
            button_obj.amount = F('amount') + 1
            button_obj.save()
