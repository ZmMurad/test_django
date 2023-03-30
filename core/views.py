from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
from core.models import MenuItem


class UrlView(DetailView):
    context_object_name="menu_object"
    template_name="template_menu.html"
    model=MenuItem
    pk_url_kwarg = 'id'