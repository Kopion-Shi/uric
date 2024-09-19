from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import MonitorHost, MonitorParams
from .serializers import MonitorParamsModelSerializer, MonitorHostModelSerlaizer


# Create your views here.
class MonitorParamViewSet(ModelViewSet):
    queryset = MonitorParams.objects.all()
    serializer_class = MonitorParamsModelSerializer


class NotificationTypeAPIView(APIView):
    def get(self, request):
        """获取监控的通知类型"""
        return Response(MonitorHost.NOTIFICATION_TYPE)

class MonitorHostViewSet(ModelViewSet):
    queryset = MonitorHost.objects.all()
    serializer_class = MonitorHostModelSerlaizer

