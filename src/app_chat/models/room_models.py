from mongoengine import StringField
from app_chat.models import TimeStamp
from app_chat.constants import CONST_ROOM_NAME_LENGTH, CONST_ROOM_TYPE_LENGTH, CONST_ROOM_TYPES, CONST_ROOM_TYPE_SINGLE

class Room(TimeStamp):
    room_name = StringField(max_length=CONST_ROOM_NAME_LENGTH, unique=True)
    room_type = StringField(max_length=CONST_ROOM_TYPE_LENGTH, choices=CONST_ROOM_TYPES, default=CONST_ROOM_TYPE_SINGLE)
