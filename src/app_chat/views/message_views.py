from app_chat.models import Message
from app_chat.serializers import MessageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MessageAPIView(APIView):
    '''
    CRUD on Message
    '''
    serializer_class = MessageSerializer
    model = Message

    def get(self, request):
        room_id = request.GET['room'] if 'room' in request.GET else None
        if room_id:
            quesyset = self.model.get_active_objects(user = room_id)
        else:
            quesyset = self.model.get_active_objects()
        data = self.serializer_class(quesyset, many=True).data
        return Response(data, status.HTTP_200_OK)      
        

    def post(self, request):
        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            message = serializer.save()
            data = self.serializer_class(message).data
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)