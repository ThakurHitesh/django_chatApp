from django.urls import path, include
from app_chat.views import ContactAPIView

urlpatterns = [
    path('friends/', ContactAPIView.as_view(), name='friends'),
]
