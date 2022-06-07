from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, UpdateAPIView

from .serializers import LoginSerializer, UserSerializer, PasswordChangeSerializer


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class PasswordChangeView(UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({"old_password": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)