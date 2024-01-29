from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from MainApp.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from MainApp.views import get_categories_for_menu
from Orders.forms import OrderCreateForm
from Orders.models import OrderItem


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(product=product, quantity=float(form_data["quantity"]), update_quantity=form_data["update"])
    return redirect("cart:cart_detail")

@require_POST
def add_product_to_cart(request):
    if request.is_ajax():
        cart = Cart(request)
        product = get_object_or_404(Product, id=int(request.POST["product_id"]))
        cart.add(product=product, quantity=float(request.POST["quantity"]))
        return HttpResponse("OK")
    return redirect("index")

def cart_detail(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"]
                )
            cart.clear()
            return render(request, "orders/created.html", {"order": order})
    else:
        return render(request, "cart/cart.html", {
        "cart": cart,
        "categories": get_categories_for_menu,
        "form": OrderCreateForm
    })

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")
