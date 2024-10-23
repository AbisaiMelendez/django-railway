from rest_framework import viewsets
from .models import Brand, Model, Series, Category, Inventory
from .serializers import BrandSerializer, ModelSerializer, SeriesSerializer, CategorySerializer, InventorySerializer
#from rest_framework import permissions
from rest_framework.permissions import AllowAny


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [AllowAny]
class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [AllowAny]
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [AllowAny]

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [AllowAny]  # Solo autenticados pueden modificar
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Solo autenticados pueden modificar
