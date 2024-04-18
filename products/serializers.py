from rest_framework import serializers
from .models import ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'parent', 'children']

    def get_children(self, obj):
        children_qs = ProductCategory.objects.filter(parent=obj)
        serializer = ProductCategorySerializer(instance=children_qs, many=True)
        return serializer.data