# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserEscuelaPadresRegisterForm, 
    EscuelaPadresLoginForm,
    PadrinoRegisterForm,
    PadrinoLoginForm
    
)

from .models import Padrino, User


###################################ESCUELA PARA PADRES#####################################################
class EscuelaPadresRegisterView(FormView):
    template_name = 'users/escuelaPadres/register.html'
    form_class = UserEscuelaPadresRegisterForm
    success_url = reverse_lazy('users_app:login-padres')

    def form_valid(self, form):
        #
        User.objects.create_userEscuelaPadres(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            ocupation=User.PADRE,
            genero=form.cleaned_data['genero'],
            
        )
        
        return super(EscuelaPadresRegisterView, self).form_valid(form)



class LoginEscuelaPadres(FormView):
    template_name = 'users/escuelaPadres/login.html'
    form_class = EscuelaPadresLoginForm
    success_url = reverse_lazy('users_app:perfil-padres')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginEscuelaPadres, self).form_valid(form)




class PerfilEscuelaParaPadres(LoginRequiredMixin,TemplateView):
    template_name='users/escuelaPadres/perfil.html'
    
    login_url = reverse_lazy('users_app:login-padres')
    
    
    
    
###################################PADRINO##########################################################




class PadrinoRegisterView(FormView):
    template_name = 'users/padrino/registerPadrino.html'
    form_class = PadrinoRegisterForm
    success_url = reverse_lazy('users_app:user-login-padrino')

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
            
        )
        
        return super(PadrinoRegisterView, self).form_valid(form)


class LoginPadrino(FormView):
    template_name = 'users/padrino/loginPadrino.html'
    form_class = PadrinoLoginForm
    success_url = reverse_lazy('users_app:user-perfil-padrino')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginPadrino, self).form_valid(form)


class PerfilPadrino(LoginRequiredMixin,TemplateView):
    template_name='users/padrino/perfilPadrino.html'
    
    login_url = reverse_lazy('users_app:user-login-padrino')











class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'home_app:inicio'
            )
        )
        











    