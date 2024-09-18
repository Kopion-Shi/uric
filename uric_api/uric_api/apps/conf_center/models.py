from django.db import models

# Create your models here.
from uric_api.utils.models import BaseModel,models
# Create your models here.
class Environment(BaseModel):
    tag = models.CharField(max_length=32,verbose_name='标识符')
    class Meta:
        app_label = 'conf_center'
        db_table = "uc_environment"
        verbose_name = "环境配置"
        verbose_name_plural = verbose_name