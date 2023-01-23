from django.urls import path
from .views import RegisterUserAPIView, login

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', login),
]



