from rest_framework.views import APIView
from app_chat.serializers import ParticipantsSerializer
from app_chat.models import Participants
from rest_framework.response import Response
from rest_framework import status

class ParticipantsAPIView(APIView):
    serializer_class = ParticipantsSerializer
    model = Participants

    def get(self, request):
        room_id = request.GET['room'] if 'room' in request.GET else None
        if room_id:
            quesyset = self.model.get_active_objects(room = room_id)
        else:
            quesyset = self.model.get_active_objects()
        data = self.serializer_class(quesyset, many=True).data
        return Response(data, status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            participants = serializer.save()
            data = self.serializer_class(participants).data
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
