from app_chat.models import Room
from app_chat.serializers import RoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RoomAPIView(APIView):
    '''
    Create room for participants
    return: room object
    '''
    serializer_class = RoomSerializer
    model = Room
    
    def post(self, request):
        #room_name = username1:username2
        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            room = serializer.save()
            data = self.serializer_class(room).data
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)