from django.shortcuts import render, get_object_or_404 ,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Horse


class HorseList(generic.ListView):
    queryset = Horse.objects.all()
    template_name = "horses_app/horses_list.html"
