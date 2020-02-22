from django.urls import path, include
from .user_urls import urlpatterns as user_urls
from .contact_urls import urlpatterns as contact_urls
from .room_urls import urlpatterns as room_urls
from .message_urls import urlpatterns as message_urls
from .participants_urls import urlpatterns as participants_urls

from app_chat.views import index, room

urlpatterns = [
    path('user/', include(user_urls), name='user'),
    path('contact/', include(contact_urls), name='contact'),
    path('roomchat/', include(room_urls), name='roomchat'),
    path('participants/', include(participants_urls), name='participants'),
    path('message/', include(message_urls), name='message'),
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room')
]
