from django.shortcuts import render, get_object_or_404
from django.views import View
from store.models.product import Product

class ProductDetail(View):
    def get(self, request, product_id):
        # Fetch the product based on the provided product_id
        product = get_object_or_404(Product, id=product_id)
        # Render the product detail template with the product information
        return render(request, 'detail.html', {'product': product})