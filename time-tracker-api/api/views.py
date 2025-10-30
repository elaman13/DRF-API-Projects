from rest_framework import generics
from app.models import Time
from .serializers import TimeSerializer
from rest_framework.response import Response


class TimeCreateView(generics.CreateAPIView):
    serializer_class = TimeSerializer


class TimeListView(generics.ListAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class TimeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

