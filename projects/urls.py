
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, ModelViewSet, SeriesViewSet, CategoryViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'models', ModelViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'inventory', InventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
