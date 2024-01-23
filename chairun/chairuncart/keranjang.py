from decimal import Decimal
from django.conf import settings # Memanggil Setting
from nisa.models import Produk # Memanggil table produk


class ChairunCart(object):
    def __init__(self, request):# menginisialisasi objek
        self.session = request.session
        chairuncart = self.session.get(settings.CHAIRUNCART_SESSION_ID)
        if not chairuncart:
            chairuncart = self.session[settings.CHAIRUNCART_SESSION_ID] = {}
        self.chairuncart = chairuncart

    def add(self, product, quantity=1, update_quantity=False): # Menyimpan data session
        product_id = str(product.id)
        if product_id not in self.chairuncart:
            self.chairuncart[product_id] = {'quantity': 0, 'price': int(product.setelah_diskon)}
        if update_quantity:
            self.chairuncart[product_id]['quantity'] = quantity
        else:
            self.chairuncart[product_id]['quantity'] += quantity
        self.save()

    def save(self): # Mengedit data session
        self.session[settings.CHAIRUNCART_SESSION_ID] = self.chairuncart
        self.session.modified = True

    def remove(self, product):# Menghapus data session
        product_id = str(product.id)
        if product_id in self.chairuncart:
            del self.chairuncart[product_id]
            self.save()

    def __iter__(self): # iterator data session
        product_ids = self.chairuncart.keys()
        products = Produk.objects.filter(id__in=product_ids)
        for product in products:
            self.chairuncart[str(product.id)]['product'] = product

        for item in self.chairuncart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self): # Menghitung quantity
        return sum(item['quantity'] for item in self.chairuncart.values())

    def get_total_price(self): # Menghitung total Harga
        return sum(Decimal(item['price']) * item['quantity'] for item in self.chairuncart.values())

    def clear(self):# Membersikan Session
        del self.session[settings.CHAIRUNCART_SESSION_ID]
        self.session.modified = True
