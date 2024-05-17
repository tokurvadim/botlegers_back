from rest_framework import serializers

from api.models import FormModel, ButtonModel, BriefModel


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModel
        fields = '__all__'


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonModel
        fields = '__all__'


class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = BriefModel
        fields = '__all__'
