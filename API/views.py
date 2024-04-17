from django.shortcuts import render
import django
from rest_framework.response import Response
from rest_framework.views import APIView
import re

from .models import Request
from core.settings import REQUEST_TYPES

class RequestHandler(APIView):
    response_data: dict = {}
    status_code: int|None = None

    def set_status_code(self, status_code) -> None:
        self.status_code = status_code

    def set_response_data(self, **kwargs) -> None:
        for key, value in kwargs:
            self.response_data[key] = value

    def get_status_code(self) -> int|None:
        return self.status_code

    def get_response_data(self) -> dict|None:
        return self.response_data

    def post(self, request) -> Response:
        #print('start1')
        try:
            #print('start2')
            data = {k: str(v)  for (k, v) in request.data.items()}
            #print(data)
            request_obj = Request(name=data.get('name'),
                                phone=data.get('phone'),
                                email=data.get('email'),
                                content=data.get('content'),
                                type=data.get('type'))
            request_obj.save()
            self.set_status_code(200)
            self.set_response_data(
                status='ok'
            )
            #print(1)
        except (django.db.utils.IntegrityError, ValueError) as error:
            error_word = error_word = re.findall(r'\.(\w+)', error.__str__())[0].upper()
            self.set_status_code(400)
            self.set_response_data(
                status='bad',
                error=f'''BAD_{error_word}'''
            )
            #print(2)
        except Exception as error:
            print(error)
            self.set_status_code = 500
            self.set_response_data({
                'status': 'bad',
                'error': 'SERVER_ERROR'
            })
            #print(3)
        finally:
            return Response(status=self.get_status_code(), data=self.get_response_data())

class RequestCounter(APIView):
    response_data: dict = {}
    status_code:int|None = None

    def set_status_code(self, status_code) -> None:
        self.status_code = status_code

    def set_response_data(self, response_data) -> None:
        self.response_data = response_data

    def get_status_code(self) -> int|None:
        return self.status_code

    def get_response_data(self) -> dict:
        return self.response_data

    def get(self, request) -> Response:
        try:
            response_data: dict = {}
            for request_type in REQUEST_TYPES:
                response_data[request_type] = Request.objects.filter(type=request_type).count()
            self.set_response_data(response_data)
            self.set_status_code(200)
        except Exception as error:
            print(error)
            self.response_data = {
                'status': 'bad',
                'error': 'SERVER_ERROR'
            }
            self.set_status_code(500)
        finally:
            return Response(data=self.get_response_data(), status=self.get_status_code())
