from rest_framework import generics
from .serializers import SignUpSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer