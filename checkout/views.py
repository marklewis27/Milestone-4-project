from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Theres nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GsC6MCMIvLgSI3ZHYmIIbzJme3gEu5F6tF3Oa4U1qgYWR3MK0JjvS0lGuUlW1R1ON3gTRzsnOyhp20mgVSNpxRK00BDU2aUr3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
