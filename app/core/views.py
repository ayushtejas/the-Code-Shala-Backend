from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.serializers import (UserSerializer,AuthSerializer)

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class AuthToken(ObtainAuthToken):
    serializer_class = AuthSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES

class UpdateUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    authentication = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
