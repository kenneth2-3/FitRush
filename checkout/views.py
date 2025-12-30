from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Sk5eeRsHSgx9SLRAL00Y5HaU9DeVxeZ4JwL66LICdFOEKK6ARn0aydhyT1XkHhwjehiPoFD2E5Y0E5bw4md1y4h00gDbKfOKX',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)