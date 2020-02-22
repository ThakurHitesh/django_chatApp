from django.urls import path, include
from app_chat.views import RoomAPIView

urlpatterns = [
    path('room-connect/', RoomAPIView.as_view(), name='room-connect'),
]
