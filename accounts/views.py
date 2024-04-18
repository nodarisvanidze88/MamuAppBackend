from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .serializers import UserSerializer
User = get_user_model()

class CustomUserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

from django.contrib.auth import authenticate

class CustomUserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_superuser:
            return Response({'error': 'You do not have permission to log in'}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)
        response = JsonResponse({
            'refffffffresh': str(refresh),
            'access': str(refresh.access_token),
        })
        response.set_cookie('refffffffresh', str(refresh))
        response.set_cookie('access', str(refresh.access_token))
        return response


class CustomUserLogout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)