import crypt
from mongoengine import Document, EmbeddedDocument, StringField, ReferenceField
from app_chat.models import TimeStamp
from app_chat.constants import *

class User(TimeStamp):
    first_name = StringField(max_length=CONST_FIRST_NAME_LENGTH)
    last_name = StringField(max_length=CONST_LAST_NAME_LENGTH)
    name = StringField(max_length=CONST_NAME_LENGTH, null=True, blank=True, required=False)
    password = StringField(max_length=CONST_PASSD_LENGTH)
    username = StringField(max_length=CONST_USERNAME_LENGTH, unique=True)
    
    def check_password(self, password):
        if crypt.crypt(password, self.password) == self.password:
            return True
        else:
            return False
 