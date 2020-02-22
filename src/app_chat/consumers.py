import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from app_chat.models import get_messages_for_room
from app_chat.models import Message, Room, User

class ChatConsumer():

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = str(self.room_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def fetch_messages(self, data):
        messages = get_messages_for_room(data['room_id'])
        content = {
            'messages': self.messages_to_json(messages)
        }
        # print(content)
        self.send_message(content)
    
    def new_message(self, data):
        room = Room.get_active_objects(id=data['room_id'])[0]
        user = User.get_active_objects(id=data['user'])[0]
        message = Message.objects.create(
            room=room,
            user=user,
            message_text=data['message_text'])
        content = {
            'message': self.message_to_json(message)
        }
        # print(content)
        return self.send_chat_message(content)
    
    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def send_message(self, message):
        self.send(text_data=json.dumps(message))
    
    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
    
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': message.id,
            'author': message.user.username,
            'content': message.message_text,
            'timestamp': str(message.created_at)
        }
