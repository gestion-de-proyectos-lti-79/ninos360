from django.shortcuts import render
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
  
    NiñoRegisterForm,
    NiñoLoginForm
    
)
from applications.users.models import User
from .models import Niño











class NiñoRegisterView(FormView):
    template_name = 'users/niño/registerNiño.html'
    form_class = NiñoRegisterForm
    success_url = reverse_lazy('niño_app:user-login-niño')

    def form_valid(self, form):
        #
        Niño.objects.create_userNiño(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            ocupation=User.NIÑO,
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
            estado=form.cleaned_data['estado'],
            municipio=form.cleaned_data['municipio'],
            phoneNumber=form.cleaned_data['phoneNumber'],
            escolaridad=form.cleaned_data['escolaridad'],
            escuela=form.cleaned_data['escuela'],
            kardex=form.cleaned_data['kardex'],
            
        )
        
        return super(NiñoRegisterView, self).form_valid(form)




class LoginNiño(FormView):
    template_name = 'users/niño/loginNiño.html'
    form_class = NiñoLoginForm
    success_url = reverse_lazy('niño_app:user-perfil-niño')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginNiño, self).form_valid(form)





class PerfilNiño(LoginRequiredMixin,TemplateView):
    template_name='users/niño/perfilNiño.html'
    
    login_url = reverse_lazy('niño_app:user-login-niño')