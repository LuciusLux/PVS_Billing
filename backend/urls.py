from rest_framework.routers import DefaultRouter
from .views import ContactApiViewSet

router = DefaultRouter()
router.register('contact', ContactApiViewSet)


urlpatterns = router.urls
