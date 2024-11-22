from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    list_display = ('id', 'name', 'about', 'created_on')
    summernote_fields = ('about',)