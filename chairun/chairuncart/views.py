from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from nisa.models import Produk
from .keranjang import ChairunCart
from .forms import ChairunCartAddProductForm


@require_POST
def chairuncart_add(request, product_id):
    chairuncart = ChairunCart(request) # create a new cart object passing it the request object
    product = get_object_or_404(Produk, id=product_id)
    quantity = int(request.POST.get('quantity'))
    form = ChairunCartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        chairuncart.add(product=product, quantity=quantity, update_quantity=cd['update'])
    return redirect('chairuncart_detail')

def chairuncart_remove(request, product_id):
    chairuncart = ChairunCart(request)
    product = get_object_or_404(Produk, id=product_id)
    chairuncart.remove(product)
    return redirect('chairuncart_detail')

def chairuncart_detail(request):
    chairuncart = ChairunCart(request)
    context = {
        'judul': 'Halaman Pemesanan Produk',
        'chairuncart':chairuncart
    }
    for item in chairuncart:
        item['update_quantity_form'] = ChairunCartAddProductForm(initial={'quantity':
        item['quantity'], 'update': True})
    return render(request, 'pemesanan.html',context)
