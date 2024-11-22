from django.shortcuts import render, get_object_or_404 
from django.views import generic
from .models import Product


class ProductsList(generic.ListView):
    queryset = Product.objects.all()
    template_name = "products_app/products_list.html"
