from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import CustomUser
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=response.data['id'])
        return Response({'token': token.key})

class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, _ = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key})
