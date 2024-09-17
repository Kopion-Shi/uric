from django.urls import path

from uric_api.apps.mtask import views

urlpatterns = [
    path('cmd_exec', views.CmdExecView.as_view()),
    path('templates', views.TemplateView.as_view()),
    path('templates/categorys', views.TemplateCategoryView.as_view()),
]
