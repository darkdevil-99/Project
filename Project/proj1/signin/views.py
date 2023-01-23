from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from .models import User
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import Signup_Serializer
from rest_framework import generics
from .models import User


# Create your views here.

class SignupAPIView(APIView):
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Register.html'

    def post(self, request):
        password = request.POST('Password', None)
        confirm_password = request.POST('Confirm Password', None)
        if password == confirm_password:
            serializer = Signup_Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
            response = status.HTTP_201_CREATED
        else:
            data = ''
            raise ValidationError(
                {'password_mismatch': 'Password fields did  not match.'}
            )
        return Response(data, status=response)


class Sign(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Register.html'
    queryset = User.objects.all()
    serializer_class = Signup_Serializer
