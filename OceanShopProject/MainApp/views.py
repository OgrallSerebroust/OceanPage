from django.core.paginator import Paginator
from random import shuffle
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
from .models import MainPageTexts, ProductType, Product, OtherPages
from Cart.forms import CartAddProductForm


def get_categories_for_menu():
    return ProductType.objects.all()


def index(request):
    # all_products_list = Product.objects.get(id = randint(1, Product.objects.count()-1))
    all_promo_list = Product.objects.order_by("?")[:9]
    most_relevanted_products = Product.objects.all()[:6]
    motto = MainPageTexts.objects.get(pk=1)
    price_benefit = MainPageTexts.objects.get(pk=2)
    sales_benefit = MainPageTexts.objects.get(pk=3)
    return render(request, "index.html", {
        "all_promo_list": all_promo_list,
        "categories": get_categories_for_menu,
        "most_relevanted_products": most_relevanted_products,
        "motto": motto,
        "price_benefit": price_benefit,
        "sales_benefit": sales_benefit
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


def about(request):
    page_content = OtherPages.objects.get(pk=1)
    return render(request, "about.html", {
        "categories": get_categories_for_menu,
        "page_content": page_content
    })


def how_to_make_order(request):
    page_content = OtherPages.objects.get(pk=2)
    return render(request, "howToMakeOrder.html", {
        "categories": get_categories_for_menu,
        "page_content": page_content
    })


def contacts(request):
    return render(request, "contacts.html", {
        "categories": get_categories_for_menu
    })


def delivery(request):
    return render(request, "delivery.html", {
        "categories": get_categories_for_menu
    })


def search(request):
    if request.is_ajax():
        searched_products = Product.objects.filter(name__icontains = request.POST["search"])
        return render(request=request, template_name="searchResultsBlock.html", context={
            "searched_products": searched_products,
            "add_to_cart_form": CartAddProductForm()
        })
    else:
        return redirect("index")
