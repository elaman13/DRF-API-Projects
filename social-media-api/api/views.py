from rest_framework import generics
from .serializers import SignUpSerializer

# Create your views here.
class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer