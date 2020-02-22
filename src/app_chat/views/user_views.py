from app_chat.models import User
from app_chat.serializers import UserSerializer, UserReadSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SignUpAPIView(APIView):
    '''
    view to register user
    '''
    serializer_class = UserSerializer

    def post(self, request):
        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            user = serializer.save()
            data = UserReadSerializer(user).data
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    '''
    view to login user
    '''
    serializer_class = UserLoginSerializer
    model = User

    def post(self, request):
        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            user = self.model.get_active_objects(username=request_data['username'])
            if user:
                user = user[0]
                if user.check_password(request_data['password']):
                    return Response(UserReadSerializer(user).data, status.HTTP_202_ACCEPTED)
            return Response({'error': 'Invalid username or password'}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)