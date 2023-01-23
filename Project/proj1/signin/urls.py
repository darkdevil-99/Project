from django.contrib import admin
from django.urls import path
from .views import SignupAPIView, Sign

urlpatterns = [
    path('', Sign.as_view(), name='signup'),


]




