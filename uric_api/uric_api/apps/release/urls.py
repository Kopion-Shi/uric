
from django.urls import path
from rest_framework import routers

from uric_api.apps.release import views

router = routers.DefaultRouter()
router.register("app", views.ReleaseAPIView, "app")
router.register("gitlab", views.GitlabAPIView, "gitlab")
router.register("jenkins", views.JenkinsAPIView, "jenkins")
urlpatterns = [

]+router.urls