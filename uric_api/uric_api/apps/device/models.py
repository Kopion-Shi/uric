from django.db import models

from uric_api.utils.models import BaseModel


# Create your models here.

class DeviceCategory(BaseModel):
    """主机类别"""

    class Meta:
        db_table = "device_category"
        verbose_name = "单板类别"
        verbose_name_plural = verbose_name  # 取消提示文字中关于英文复数+s的情况


class Pdu(BaseModel):
    pdu_category = models.CharField(max_length=50, verbose_name='pdu类型')
    ip = models.CharField(blank=True, null=True, max_length=255, verbose_name='连接地址')

    class Meta:
        db_table = "pdu_detail"
        verbose_name = "pdu"
        verbose_name_plural = verbose_name  # 取消提示文字中关于英文复数+s的情况


class ShareHost(BaseModel):
    ip = models.CharField(blank=True, null=True, max_length=255, verbose_name='连接地址')

    class Meta:
        db_table = "sharehost_detail"
        verbose_name = "串口服务器"
        verbose_name_plural = verbose_name  # 取消提示文字中关于英文复数+s的情况


class Device(BaseModel):
    # 真正在数据库中的字段实际上叫 category_id，而category则代表了关联的哪个分类模型对象
    category = models.ForeignKey('Device', on_delete=models.DO_NOTHING, verbose_name='单板类别', related_name='dc',
                                 null=True, blank=True)
    ip_addr = models.CharField(blank=True, null=True, max_length=255, verbose_name='连接地址')
    port = models.IntegerField(verbose_name='端口', default=22)
    username = models.CharField(max_length=50, verbose_name='登录用户')
    password = models.CharField(max_length=50, verbose_name='登录密码', )

    pdu = models.ForeignKey('Pdu', on_delete=models.DO_NOTHING, verbose_name='pdu', related_name='pc',
                            null=True, blank=True)
    pdu_port = models.IntegerField(verbose_name='端口', default=0)

    share_host = models.ForeignKey('ShareHost', on_delete=models.DO_NOTHING, verbose_name='share_host',
                                   related_name='sc',
                                   null=True, blank=True)
    sharehost_port = models.IntegerField(verbose_name='端口', default=0)

    class Meta:
        db_table = "device"
        verbose_name = "单板信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + ':' + self.ip_addr
