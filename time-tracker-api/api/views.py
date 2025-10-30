from rest_framework import generics
from app.models import Time
from .serializers import TimeSerializer, TimeListSerializer
from rest_framework.response import Response


class TimeCreateView(generics.CreateAPIView):
    serializer_class = TimeSerializer


class TimeListView(generics.ListAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeListSerializer

class TimeView(generics.GenericAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeListSerializer

    def get(self, request, pk=None):
        if pk:
            serializer = self.get_serializer(self.get_object())
        else:
            serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(serializer.data)
    
    def patch(self, request, pk):
        time = self.get_object()
        serializer = TimeSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
