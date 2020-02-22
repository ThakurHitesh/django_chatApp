from django.urls import path, include
from app_chat.views import MessageAPIView

urlpatterns = [
    path('message-connect/', MessageAPIView.as_view(), name='message-connect'),
]
