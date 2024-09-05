from django.shortcuts import render, get_object_or_404 ,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Product


class ProductsList(generic.ListView):
    queryset = Product.objects.all()
    template_name = "products_app/products_list.html"
