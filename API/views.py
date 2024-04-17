import django
import re
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Request
from .serializers import RequestSerializer
from core.settings import REQUEST_TYPES

class RequestHandler(APIView):
    response_data: dict = {}
    status_code: int|None = None

    def post(self, request) -> Response:
        #print('start1')
        try:
            #print('start2')
            data = {k: v for (k, v) in request.data.items() if len(v) != 0}
            #print(data)

            serializer = RequestSerializer(data=data)
            serializer.is_valid()
            serializer.save()

            self.status_code = 200
            self.response_data = {
                'ok': True
            }
            #print(1)
        except AssertionError as error:
            #print(error_word)
            self.status_code = 404
            self.response_data = {
                'ok': False,
                'error': 'INVALID_DATA'
            }
            #print(2)
        except Exception as error:
            print(error)
            self.status_code = 500
            self.response_data = {
                'status': 'bad',
                'error': f'SERVER_ERROR'
            }
            #print(3)
        finally:
            #print('final')
            return Response(status=self.status_code, data=self.response_data)

class RequestCounter(APIView):
    response_data: dict = {}
    status_code:int|None = None

    def get(self, request) -> Response:
        try:
            for request_type in REQUEST_TYPES:
                self.response_data[request_type] = Request.objects.filter(type=request_type).count()
            self.status_code = 200
            self.response_data = {
                'ok': True,
                'content': self.response_data
            }
        except Exception as error:
            print(error)
            self.response_data = {
                'ok': False,
                'error': 'SERVER_ERROR'
            }
            self.status_code = 500
        finally:
            return Response(data=self.response_data, status=self.status_code)
