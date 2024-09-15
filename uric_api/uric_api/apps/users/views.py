from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serlializer import CustomTokenObtainPairSerializer, UserInfoSerializer


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserInfoView(generics.ListAPIView):
    queryset = User.objects
    serializer_class = UserInfoSerializer

    def get(self, request, *args, **kwargs):
        # data = super().p()
        # 在这里自定义返回的数据结构
        new_data = {
            'code': 20000,
            'data': {
                'roles': ['admin'],
                'introduction': 'I am a super administrator',
                'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                'name': 'Super Admin'
            }}

        return Response(new_data)


class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({'code': 20000, 'data': 'Logout successful'})
