from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from MainApp.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from MainApp.views import get_categories_for_menu

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(product=product, quantity=form_data["quantity"], update_quantity=form_data["update"])
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart.html", {"cart": cart,
        "categories": get_categories_for_menu})

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")
