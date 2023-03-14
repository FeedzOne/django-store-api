from rest_framework import routers
from .api import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register('api/products', ProductViewSet, 'products')
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls

