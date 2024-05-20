from django.urls import path
from .views import GetListCreateFormAPIView, GetButtonsListAPIView,GetListCreateBriefAPIView, GetListCreateAboutUsAPIView

urlpatterns = [
    path('form/', GetListCreateFormAPIView.as_view()),
    path('list/', GetButtonsListAPIView.as_view()),
    path('brief/', GetListCreateBriefAPIView.as_view()),
    path('aboutus/', GetListCreateAboutUsAPIView.as_view())
]
