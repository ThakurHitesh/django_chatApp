from rest_framework_mongoengine.serializers import DocumentSerializer
from app_chat.models import Contact

class ContactSerializer(DocumentSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'created_at', 'user','friends']