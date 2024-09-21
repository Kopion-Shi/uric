from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from uric_api.apps.conf_center.models import Environment
from uric_api.apps.conf_center.serializers import EnvironmentModelSerializer


# Create your views here.
class EnvironmentAPIView(ModelViewSet):
    """
       环境管理的api接口
       """
    queryset = Environment.objects.all()
    serializer_class = EnvironmentModelSerializer
    permission_classes = [IsAuthenticated]