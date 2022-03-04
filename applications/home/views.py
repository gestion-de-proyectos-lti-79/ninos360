from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)


class HomeView(TemplateView):
    template_name = 'home/inicio.html'
    
    
class NoAccesoView(TemplateView):
    template_name = 'home/noaccess.html'
    
    
