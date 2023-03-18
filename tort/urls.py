from rest_framework.routers import DefaultRouter

from .views import (
    AirportViewSet,
    CompanyViewSet,
)

router = DefaultRouter()
router.register('airport',AirportViewSet,basename='airport')
router.register('company',CompanyViewSet,basename='company')

urlpatterns = router.urls