from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
# Create your views here.

stripe_api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.checkout == "POST ":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                products = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity,
                )
                order_line_item.save()

            try: