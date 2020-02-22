from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app_chat.routing import urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            urlpatterns
        )
    )
})