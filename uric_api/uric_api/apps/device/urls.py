from rest_framework import routers

from .views import DeviceView, PduView, ShareHostView, Categorys

urlpatterns = []
router = routers.DefaultRouter()
router.register('detail', DeviceView)
router.register('pdu', PduView)
router.register('sharehost', ShareHostView)
router.register('categorys', Categorys)

urlpatterns += router.urls
