from typing import Any

from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import FormModel
from api.serializers import FormSerializer


class GetListCreateFormAPIView(ListCreateAPIView):
    serializer_class = FormSerializer
    queryset = FormModel.objects.all()

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data={"total_orders": queryset.count(), "data": serializer.data})
