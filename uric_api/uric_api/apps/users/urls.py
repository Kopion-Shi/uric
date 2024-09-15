from django.urls import path
from rest_framework_simplejwt.views import token_verify, token_refresh

from .views import CustomTokenObtainPairView, UserInfoView,LogoutView

urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('info', UserInfoView.as_view(), name='loginfo'),
    path('verify/', token_verify),  # 这是只是校验token有效性
    path('refresh_jwt_token/', token_refresh),  # 校验并生成新的token
]
