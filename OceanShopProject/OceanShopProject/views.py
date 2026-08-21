from django.shortcuts import render
from MainApp.models import OtherPages
from MainApp.views import get_categories_for_menu

def page_not_found_view(request, exception):
    page_content = OtherPages.objects.get(pk=3)
    return render(request, "404.html", {
        "categories": get_categories_for_menu,
        "page_content": page_content
    }, status=404)