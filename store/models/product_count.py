from .product import Product
from django.db import models

class ProductRetrieval(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    retrieval_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} retrieved on {self.retrieval_time}"