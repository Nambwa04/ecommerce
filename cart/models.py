from django.db import models
from products.models import Product

# Create your models here.

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
