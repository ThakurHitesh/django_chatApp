from rest_framework_mongoengine.serializers import DocumentSerializer
from app_chat.models import Participants

class ParticipantsSerializer(DocumentSerializer):
    class Meta:
        model = Participants
        fields = ['id', 'created_at', 'user', 'room']