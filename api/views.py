from typing import Any

from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from api.models import FormModel, ButtonModel, BriefModel, AboutUsModel, PortfolioModel
from api.serializers import FormSerializer, ButtonSerializer, BriefSerializer, AboutUsSerializer, PortfolioSerializer


class GetListCreateFormAPIView(ListCreateAPIView):
    serializer_class = FormSerializer
    queryset = FormModel.objects.all()

    """def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        button_name = request.data.get('button')
        if button_name:
            ButtonModel.update_amount(ButtonModel, button_name=button_name)
        else:
            raise ValidationError({
                'button': [
                    'This field may not be null.'
                ]
            })

        return super().create(request=request, args=args, kwargs=kwargs)"""
    

class GetListCreateBriefAPIView(ListCreateAPIView):
    queryset = BriefModel.objects.all()
    serializer_class = BriefSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        button_name = request.data.get('button')
        if button_name:
            ButtonModel.update_amount(ButtonModel, button_name=button_name)
        else:
            raise ValidationError({
                'button': [
                    'This field may not be null.'
                ]
            })

        return super().create(request=request, args=args, kwargs=kwargs)


class GetButtonsListAPIView(ListAPIView):
    queryset = ButtonModel.objects.all()
    serializer_class = ButtonSerializer


class GetListCreateAboutUsAPIView(ListCreateAPIView):
    queryset = AboutUsModel.objects.all()
    serializer_class = AboutUsSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    


class GetListCreatePortfolioAPIView(ListCreateAPIView):
    queryset = PortfolioModel.objects.all()
    serializer_class = PortfolioSerializer

