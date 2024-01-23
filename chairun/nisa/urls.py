from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('profil', views.profil, name='profil'),
    path('hubungi-kami', views.KontakView.as_view(), name='kontak'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    
    path('<slug:kategori_slug>/<slug:slug>', views.produk, name='produk'),
    path('<slug:slug>', views.kategori, name='kategori'),
]
