from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from uric_api.apps.users.models import User
from uric_api.apps.users.serlializer import CustomTokenObtainPairSerializer, UserInfoSerializer


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserInfoView(generics.ListAPIView):
    queryset = User.objects
    serializer_class = UserInfoSerializer

    def get(self, request, *args, **kwargs):
        # 在这里自定义返回的数据结构
        data = {
                'roles': ['admin'],
                'introduction': 'I am a super administrator',
                'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                'name':''
            }

        return Response(data)


class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({'code': 20000, 'data': 'Logout successful'})
