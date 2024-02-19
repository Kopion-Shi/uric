# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Device, Pdu, ShareHost,DeviceCategory
from .serializers import DeviceSerializer, ShareHostSerializer, PduSerializer, DeviceCategorySerializer

class Categorys(ModelViewSet):
    queryset = DeviceCategory.objects
    serializer_class = DeviceCategorySerializer

class DeviceView(ModelViewSet):
    queryset = Device.objects
    serializer_class = DeviceSerializer


class PduView(ModelViewSet):
    queryset = Pdu.objects
    serializer_class = PduSerializer


class ShareHostView(ModelViewSet):
    queryset = ShareHost.objects
    serializer_class = ShareHostSerializer
