from rest_framework import serializers

from api.models import FormModel


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModel
        fields = '__all__'
