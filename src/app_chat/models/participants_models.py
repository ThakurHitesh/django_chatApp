from app_chat.models import TimeStamp, User, Room
from mongoengine import ReferenceField

class Participants(TimeStamp):
    user = ReferenceField(User, dbref=True)
    room = ReferenceField(Room, dbref=True)
    meta = {
        'indexes':[
            {'fields':('user', 'room'), 'unique':True}
        ]
    }