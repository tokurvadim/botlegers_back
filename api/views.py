from typing import Any

from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from api.models import FormModel, RequestType
from api.serializers import FormSerializer, RequestSerializer


class GetListCreateFormAPIView(ListCreateAPIView):
    serializer_class = FormSerializer
    queryset = FormModel.objects.all()

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data={"total_orders": queryset.count(), "data": serializer.data})
    
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        request_type_obj = RequestType.objects.get_or_create(type=request.data.get('type'))[0]

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        request_type_obj.amount += 1
        request_type_obj.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class GetRequestTypeListAPIView(ListAPIView):
    queryset = RequestType.objects.all()
    serializer_class = RequestSerializer
