from rest_framework.serializers import ModelSerializer

from .models import Device, Pdu, ShareHost, DeviceCategory


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class PduSerializer(ModelSerializer):
    class Meta:
        model = Pdu
        fields = '__all__'


class ShareHostSerializer(ModelSerializer):
    class Meta:
        model = ShareHost
        fields = '__all__'
class DeviceCategorySerializer(ModelSerializer):
    class Meta:
        model = DeviceCategory
        fields = '__all__'
