from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework import generics
from .models import User1
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

# Create your views here.
'''
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            user = User1.objects.get(id=request.user.id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except user.DoNotExist:
            user = None
'''


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User1.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("Username")
    password = request.data.get("Password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    x = User1.objects.all()
    c = 0
    while c < len(x):
        y = x[c]
        # user = authenticate(username=y.Username, password=y.Password, user_id=y.id)
        if y.Username == username and y.Password == password:
            token, _ = Token.objects.get_or_create()
            y.Token = token.key
            y.save()
            return Response({'token': token.key, 'Success': 'Logged-in Successfully'},
                            status=HTTP_200_OK)
        c += 1
    else:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)

















