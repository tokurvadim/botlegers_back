from typing import Any

from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import FormModel, ButtonModel, BriefModel
from api.serializers import FormSerializer, ButtonSerializer, BriefSerializer


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
    serializer_class = BriefSerializer
    queryset = BriefModel.objects.all()

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
