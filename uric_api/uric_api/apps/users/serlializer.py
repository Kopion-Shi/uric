from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from uric_api.apps.users.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # 在这里自定义返回的数据结构
        new_data = {
            'code': 20000,
            'data': {
                'user_id': self.user.id,
                'username': self.user.username,
                'token': data['refresh']
            }
        }
        return new_data


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name','mobile','avatar')

