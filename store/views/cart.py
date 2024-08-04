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
        # Get the product ID and action from the request
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        cart = request.session.get('cart', {})

        if product_id:
            product_id = str(product_id)  # Ensure product_id is a string to match session keys
            if action == 'increase':
                # Increase the product quantity by 1
                cart[product_id] = cart.get(product_id, 0) + 1
            elif action == 'decrease':
                # Decrease the product quantity by 1
                if cart.get(product_id, 0) > 1:
                    cart[product_id] -= 1
                else:
                    # Remove the product if quantity is 0 or less
                    cart.pop(product_id, None)
            elif action == 'remove':
                # Remove the product from the cart
                cart.pop(product_id, None)

            # Update the session cart
            request.session['cart'] = cart

        return redirect('cart')
