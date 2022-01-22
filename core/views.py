from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import serializers
import json
from .models import *
from django.http import JsonResponse

# Create your views here.


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = LoginSerializers

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        if username is None and password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        # if User.is_authenticated:
        #     print(User.objects.get(username=username).id)
        #     token, _ = Token.objects.get_or_create(user=User.objects.get(username=username).id)
        #     return Response({ "Message": "Already Authenticated!",'token': token.key},
        #                 status=status.HTTP_200_OK)
        user = authenticate(username=username, password=password)
        login(request,user)
        print(type(user))
        if not user:
            return Response({'error': 'Invalid credentials'},
                            status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        print(token.key)
        # Token.save()
        return Response({ "Message": "Login successful!",'token': token.key},
                        status=status.HTTP_200_OK)


class Logout(generics.GenericAPIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        Token.objects.filter(user=request.user.id).delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateSerializer


class ReadView(generics.ListAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReadSerializer


class ReadIndividualView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReadSerializer


class CreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateSerializer
    permission_classes = (IsAuthenticated, )


class DeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DeleteSerializer