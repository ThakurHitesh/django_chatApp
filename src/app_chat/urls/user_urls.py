from django.urls import path, include
from app_chat.views import SignUpAPIView, LoginAPIView

urlpatterns = [
    path('register/', SignUpAPIView.as_view(), name='user-signup'),
    path('login/', LoginAPIView.as_view(), name='user-signin'),
]
