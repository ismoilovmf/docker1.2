from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, ProductPositionSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
router.register('productpositions', ProductPositionSet)
urlpatterns = router.urls
