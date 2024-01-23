from django.urls import path
from . import views

urlpatterns = [
    path('add/<product_id>', views.chairuncart_add, name='chairuncart_add'),
    path('remove/<product_id>', views.chairuncart_remove, name='chairuncart_remove'),
    path('', views.chairuncart_detail, name='chairuncart_detail'),


]