from django.urls import path, include
from app_chat.views import ParticipantsAPIView

urlpatterns = [
    path('participants-connect/', ParticipantsAPIView.as_view(), name='participants-connect'),
]
