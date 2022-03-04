from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
#
from .models import User


def check_ocupation_user(ocupation, user_ocupation):
    #
    
    if (ocupation == User.ADMINISTRADOR or ocupation == user_ocupation):
        
        return True
    else:
        return False


class PadrinoPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #
        if not check_ocupation_user(request.user.ocupation, User.PADRINO):
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'users_app:user-login'
                )
            )

        return super().dispatch(request, *args, **kwargs)


class EscuelaPadresPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #
        if not check_ocupation_user(request.user.ocupation, User.PADRE):
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'home_app:no-access'
                )
            )
        return super().dispatch(request, *args, **kwargs)


class AdminPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #
        if not check_ocupation_user(request.user.ocupation, User.ADMINISTRADOR):
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'users_app:user-login'
                )
            )
        return super().dispatch(request, *args, **kwargs)
        
