from django.urls import path
from .views import GetListCreateFormAPIView, GetRequestTypeListAPIView

urlpatterns = [
    path('form/', GetListCreateFormAPIView.as_view()),
    path('list/', GetRequestTypeListAPIView.as_view())
]
