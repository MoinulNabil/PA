from django.db import models
from django.conf import settings


class ProductCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ['title']


class Product(models.Model):
    vendor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='products',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        ProductCategory,
        related_name='products',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    

class Color(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title
    

class ProductColor(models.Model):
    color = models.ForeignKey(
        Color,
        related_name='products',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='colors',
        on_delete=models.CASCADE
    )
    stock = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.product.title} with color {self.color.title}"
    

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='product_images')

    def __str__(self) -> str:
        return self.product.title
