from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product

def _get_cart(request):
    """Return the cart dict from session. Keys are product ids (str), values are quantities (int)."""
    return request.session.get('cart', {})

def _save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True

def _cart_item_count(request):
    cart = _get_cart(request)
    return sum(cart.values())

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'cart_count': _cart_item_count(request),
        'total_products': products.count(),
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'cart_count': _cart_item_count(request),
    }
    return render(request, 'shop/product_detail.html', context)

def add_to_cart(request, pk):
    # allow POST and GET for convenience
    product = get_object_or_404(Product, pk=pk)
    cart = _get_cart(request)
    key = str(product.pk)
    cart[key] = cart.get(key, 0) + 1
    _save_cart(request, cart)
    # redirect back to cart
    return redirect(reverse('shop:cart_view'))

def remove_from_cart(request, pk):
    cart = _get_cart(request)
    key = str(pk)
    if key in cart:
        # remove the item entirely
        del cart[key]
        _save_cart(request, cart)
    return redirect(reverse('shop:cart_view'))

def cart_view(request):
    cart = _get_cart(request)
    items = []
    total = Decimal('0.00')
    for pid_str, qty in cart.items():
        try:
            p = Product.objects.get(pk=int(pid_str))
        except Product.DoesNotExist:
            continue
        subtotal = p.price * qty
        items.append({
            'product': p,
            'quantity': qty,
            'subtotal': subtotal,
        })
        total += subtotal
    context = {
        'items': items,
        'total': total,
        'cart_count': _cart_item_count(request),
    }
    return render(request, 'shop/cart.html', context)
