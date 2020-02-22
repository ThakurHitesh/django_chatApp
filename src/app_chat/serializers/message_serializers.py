from rest_framework_mongoengine.serializers import DocumentSerializer
from app_chat.models import Message

class MessageSerializer(DocumentSerializer):
    class Meta:
        model = Message
        fields = ['id', 'created_at', 'room', 'user', 'message_text']