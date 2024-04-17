from django.urls import path
from .views import CreateFormAPIView, GetFormListAPIView

urlpatterns = [
    path('send/', CreateFormAPIView.as_view()),
    path('count/', GetFormListAPIView.as_view())
]
