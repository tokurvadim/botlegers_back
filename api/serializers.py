from rest_framework import serializers

from api.models import FormModel, RequestType


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModel
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestType
        fields = '__all__'
