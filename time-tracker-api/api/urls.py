from django.urls import path
from .views import TimeCreateView, TimeListView, TimeView

urlpatterns = [
    path('time/', TimeCreateView.as_view(), name='time'),
    path('times/', TimeListView.as_view(), name='times'),
    path('times/<int:pk>/', TimeView.as_view(), name='time-detail'),
]
