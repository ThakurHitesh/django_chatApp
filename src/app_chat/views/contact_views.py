from app_chat.models import Contact
from app_chat.serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ContactAPIView(APIView):
    '''
    CRUD on contact
    '''
    serializer_class = ContactSerializer
    model = Contact

    def get(self, request):
        user_id = request.GET['user'] if 'user' in request.GET else None
        if user_id:
            quesyset = self.model.get_active_objects(user = user_id)
        else:
            quesyset = self.model.get_active_objects()
        data = self.serializer_class(quesyset, many=True).data
        return Response(data, status.HTTP_200_OK)      
        

    def post(self, request):
        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            contact = serializer.save()
            data = self.serializer_class(contact).data
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        request_data = request.data
        user_id = request_data.pop('user')
        instance = self.model.get_active_objects(user = user_id)[0]
        serializer = self.serializer_class(instance, data=request_data, partial=True)
        if serializer.is_valid():
            contact = serializer.save()
            data = self.serializer_class(contact).data
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
