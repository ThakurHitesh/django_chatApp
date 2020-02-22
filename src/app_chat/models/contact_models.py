from mongoengine import Document, EmbeddedDocument, ReferenceField, ListField, EmbeddedDocument
from app_chat.models import User, TimeStamp

class Contact(TimeStamp):
    user = ReferenceField(User, dbref=True, unique=True)
    friends = ListField(ReferenceField(User, dbref=True), blabk=True, null=True, required=False)

    def __str__(self):
        return self.user.name