from django.urls import path
from .views import RequestCounter, RequestHandler

urlpatterns = [
    path('send/', RequestHandler.as_view()),
    path('count/', RequestCounter.as_view())
]