from django.urls import path
from rest_framework.routers import DefaultRouter
from uric_api.apps.conf_center import views

router = DefaultRouter()
router.register("env", views.EnvironmentAPIView, basename="env")

urlpatterns = [

] + router.urls