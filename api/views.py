from rest_framework.generics import CreateAPIView, ListAPIView

from api.models import FormModel
from api.serializers import FormSerializer


class CreateFormAPIView(CreateAPIView):
    serializer_class = FormSerializer
    queryset = FormModel


class GetFormListAPIView(ListAPIView):
    serializer_class = FormSerializer
    queryset = FormModel.objects.all()
