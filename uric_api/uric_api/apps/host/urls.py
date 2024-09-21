from django.urls import path, re_path

from uric_api.apps.host.views import HostModelViewSet, HostCategoryListAPIView, ExcelHostView

urlpatterns = [
    path('', HostModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    re_path('(?P<pk>\d+)', HostModelViewSet.as_view({'delete': 'destroy'})),
    path('category', HostCategoryListAPIView.as_view()),
    path('excel_host', ExcelHostView.as_view()),
]
