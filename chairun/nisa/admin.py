from django.contrib import admin
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis, ChatID

class DataKategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif","banner_satu","banner_dua",)
    prepopulated_fields = {"slug": ("nama",)}

class ProdukAdmin(admin.ModelAdmin):
    list_display = ("nama_produk", "gambar","harga","no_whatsup",)
    prepopulated_fields = {"slug": ("nama_produk",)}
    

admin.site.register(Kategori,DataKategoriAdmin)
admin.site.register(Produk,ProdukAdmin)
admin.site.register(Slide)
admin.site.register(Kontak)
admin.site.register(Profil)
admin.site.register(ChatID)


