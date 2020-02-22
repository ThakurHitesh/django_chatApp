from app_chat.models import Message

def get_messages_for_room(room_id):
    queryset = Message.get_active_objects(room=room_id)
    return queryset