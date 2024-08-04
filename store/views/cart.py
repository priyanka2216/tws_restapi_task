from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request):
        # Get the product IDs from the cart stored in the session
        cart = request.session.get('cart', {})
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
    
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        cart = request.session.get('cart', {})

        if product_id:
            product_id = str(product_id)  # Ensure product_id is a string to match session keys
            if action == 'increase':
                
                cart[product_id] = cart.get(product_id, 0) + 1
            elif action == 'decrease':
                
                if cart.get(product_id, 0) > 1:
                    cart[product_id] -= 1
                else:
                    
                    cart.pop(product_id, None)
            elif action == 'remove':

                cart.pop(product_id, None)

            request.session['cart'] = cart

        return redirect('cart')
