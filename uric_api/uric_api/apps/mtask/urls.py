from django.urls import path

from uric_api.apps.mtask import views

urlpatterns = [
    path('cmd_exec', views.CmdExecView.as_view(), name='cmd_exec'),
    path('templates', views.TemplateView.as_view(), name='templates'),
    path('templates/categorys', views.TemplateCategoryView.as_view(), name='templates_categorys'),
]
