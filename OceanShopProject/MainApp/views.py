from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from random import randint
from .models import ProductType, Product
from Cart.forms import CartAddProductForm


def get_categories_for_menu():
    return ProductType.objects.all()


def index(request):
    all_products_list = Product.objects.get(id = randint(1, Product.objects.count()-1))
    most_relevanted_products = Product.objects.all()[:6]
    return render(request, "index.html", {
        "all_products_list": all_products_list,
        "categories": get_categories_for_menu,
        "most_relevanted_products": most_relevanted_products
    })


def catalog(request):
    category = request.GET.get("category")
    try:
        products_list = Product.objects.filter(product_type_id = category)
    except ValueError:
        products_list = Product.objects.filter(product_type_id = 1)
    paginate_frozen_fish_products = Paginator(products_list, 12)
    page_number = request.GET.get("page_number")
    page_data = paginate_frozen_fish_products.get_page(page_number)
    return render(request, "catalog.html", {
        "category": category,
        "categories": get_categories_for_menu,
        "page_range": paginate_frozen_fish_products.get_elided_page_range(number=page_data.number, on_each_side=2),
        "page_data": page_data,
        "add_to_cart_form": CartAddProductForm()
    })


def contacts(request):
    return render(request, "contacts.html", {
        "categories": get_categories_for_menu
    })


def delivery(request):
    return render(request, "delivery.html", {
        "categories": get_categories_for_menu
    })
