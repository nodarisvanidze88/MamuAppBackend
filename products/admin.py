from django.contrib import admin
from .models import ProductCategory, Product, ProductImage
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)