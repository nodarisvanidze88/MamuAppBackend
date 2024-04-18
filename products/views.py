from rest_framework import viewsets
from .models import ProductCategory
from .serializers import ProductCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.filter(parent=None)
    serializer_class = ProductCategorySerializer