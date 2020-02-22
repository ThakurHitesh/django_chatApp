from mongoengine import ReferenceField, StringField
from app_chat.constants import CONST_MESSAGE_LENGTH
from app_chat.models import Room, User, TimeStamp

class Message(TimeStamp):
    room = ReferenceField(Room, dbref=True)
    user = ReferenceField(User, dbref=True)
    message_text = StringField(max_length=CONST_MESSAGE_LENGTH)

