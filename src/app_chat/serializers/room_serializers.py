from rest_framework_mongoengine.serializers import DocumentSerializer
from app_chat.models import Room

class RoomSerializer(DocumentSerializer):
    class Meta:
        model = Room
        fields = ['id', 'created_at', 'room_name', 'room_type']