from django.urls import path
from .views import GetListCreateFormAPIView

urlpatterns = [
    path('form/', GetListCreateFormAPIView.as_view()),
]
