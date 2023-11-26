from django.db import models
from django.conf import settings

from shopping_cart.models import Shop



class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='orders',
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(Shop, blank=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=13)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=10)
    notes = models.TextField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email