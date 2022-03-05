from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic.edit import (
    FormView
)
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
  
    PadrinoRegisterForm,
    PadrinoLoginForm
    
)
from applications.users.models import User
from .models import Padrino
# Create your views here.








class PadrinoRegisterView(FormView):
    template_name = 'users/padrino/registerPadrino.html'
    form_class = PadrinoRegisterForm
    success_url = reverse_lazy('padrino_app:user-login-padrino')

    def form_valid(self, form):
        #
        Padrino.objects.create_userPadrino(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            ocupation=User.PADRINO,
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
            estado=form.cleaned_data['estado'],
            municipio=form.cleaned_data['municipio'],
            phoneNumber=form.cleaned_data['phoneNumber'],
            estadoCivil=form.cleaned_data['estadoCivil'],
            escolaridad=form.cleaned_data['escolaridad'],
            
        )
        
        return super(PadrinoRegisterView, self).form_valid(form)




class LoginPadrino(FormView):
    template_name = 'users/padrino/loginPadrino.html'
    form_class = PadrinoLoginForm
    success_url = reverse_lazy('padrino_app:user-perfil-padrino')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginPadrino, self).form_valid(form)





class PerfilPadrino(LoginRequiredMixin,TemplateView):
    template_name='users/padrino/perfilPadrino.html'
    
    login_url = reverse_lazy('padrino_app:user-login-padrino')