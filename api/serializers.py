from rest_framework import serializers

from api.models import FormModel, ButtonModel


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModel
        fields = '__all__'


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonModel
        fields = '__all__'
