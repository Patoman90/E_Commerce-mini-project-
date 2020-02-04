from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """View that renders contents page."""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """View that adds a item to the cart."""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.seesion['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """View that allows you to adjust the specified amount of a specified product."""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.seesion['cart'] = cart
    return redirect(reverse('view_cart'))
