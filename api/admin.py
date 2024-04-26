from django.contrib import admin

from api.models import FormModel, ButtonModel


@admin.register(FormModel)
class FormAdmin(admin.ModelAdmin):
    pass


@admin.register(ButtonModel)
class ButtonAdmin(admin.ModelAdmin):
    pass
