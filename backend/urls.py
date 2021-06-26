from rest_framework.routers import DefaultRouter
from .views import ContactApiViewSet, AddressApiView, InvoiceApiView, InvoicePositionApiView, CountryApiView

router = DefaultRouter()
router.register('contact', ContactApiViewSet)
router.register('address', AddressApiView)
router.register('invoice', InvoiceApiView)
router.register('invoiceposition', InvoicePositionApiView)
router.register('country', CountryApiView)

urlpatterns = router.urls