from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# (a) Product list and last viewed cookie
def product_list(request):
    last_viewed_id = request.COOKIES.get("last_product_id")
    context = {
        "products": Product.objects.all(),
        "last_viewed_id": last_viewed_id,
    }
    return render(request, "shop/product_list.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    response = render(request, "shop/product_detail.html", {"product": product})
    # Save cookie for last viewed product
    response.set_cookie("last_product_id", product.id, max_age=60*60*24*7)  # 7 days
    return response

def redirect_to_last_product(request):
    last_viewed_id = request.COOKIES.get("last_product_id")
    if last_viewed_id:
        return redirect("product_detail", pk=last_viewed_id)
    return redirect("product_list")

# (b) Background color preference
def color_preference(request):
    selected_color = request.COOKIES.get("bg_color", "white")  # default white
    if request.method == "POST":
        selected_color = request.POST.get("color")
        response = render(request, "shop/color_preference.html", {"selected_color": selected_color})
        response.set_cookie("bg_color", selected_color, max_age=60*60*24*30)  # 30 days
        return response
    return render(request, "shop/color_preference.html", {"selected_color": selected_color})
