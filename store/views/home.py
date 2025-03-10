from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print("cart:", request.session['cart'])

        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_products_by_categoryid(category_id)
        else:
            products = Product.get_all_products()
        categories = Category.get_all_categories()

        data = {
            'products': products,
            'categories': categories,
        }
        return render(request, "index.html", data)
