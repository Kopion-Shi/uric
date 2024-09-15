from django.urls import path
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.views import token_verify, token_obtain_pair, token_refresh, TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # 在这里自定义返回的数据结构
        new_data={
            'code':20000,
            'data':{
                'user_id': self.user.id,
                'username':self.user.username,
                'token':data['refresh']
            }
        }
        return new_data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('verify/', token_verify),  # 这是只是校验token有效性
    path('refresh_jwt_token/', token_refresh),  # 校验并生成新的token
]