from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("param", views.MonitorParamViewSet, basename="param")
router.register("host", views.MonitorHostViewSet, basename="host")

urlpatterns = [
                  path("notif/", views.NotificationTypeAPIView.as_view()),
              ] + router.urls
