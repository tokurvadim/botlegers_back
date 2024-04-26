from django.urls import path
from .views import GetListCreateFormAPIView, GetButtonsListAPIView

urlpatterns = [
    path('form/', GetListCreateFormAPIView.as_view()),
    path('list/', GetButtonsListAPIView.as_view())
]
