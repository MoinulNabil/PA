from django.contrib import admin

from .models import (
    Product,
    Color,
    ProductCategory,
    ProductColor,
    ProductImage
)


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
