from django.db import models

# Create your models here.
from uric_api.utils.models import BaseModel, models
from uric_api.apps.users.models import User


# Create your models here.
class ReleaseApp(BaseModel):
    tag = models.CharField(max_length=32, unique=True, verbose_name='应用唯一标识号')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        db_table = "release_app"
        app_label = "release"
        verbose_name = "应用管理"
        verbose_name_plural = verbose_name