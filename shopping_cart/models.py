from django.db import models
from django.conf import settings

from product.models import ProductColor


class Shop(models.Model):
    """Model to track/store items added to the cart"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='shop_items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        ProductColor,
        on_delete=models.CASCADE
    )
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return f"{self.product.product.title} x {self.quantity}"
    
    @property
    def total_amount(self):
        return self.quantity * self.price


class Cart(models.Model):
    """
    User cart
    Every user will have a signle cart entry at a time
    When the order will be complete, it will be deleted.
    And a new cart entry will be reissued upon adding new shop items next time
    
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='cart',
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(Shop, blank=True)

    def __str__(self) -> str:
        return self.user.email
