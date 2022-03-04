#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    
    ###########################PADRES##########################################################
    path(
        'login/escuela/padres/', 
        views.LoginEscuelaPadres.as_view(),
        name='login-padres',
    ),
    path(
        'users/register/escuela/padres/', 
        views.EscuelaPadresRegisterView.as_view(),
        name='register-padres',
    ),
    
    path(
        'users/perfil/padres/', 
        views.PerfilEscuelaParaPadres.as_view(),
        name='perfil-padres',
    ),
    
    #############################################PADRINO#################################
    path(
        'users/padrino/register/', 
        views.PadrinoRegisterView.as_view(),
        name='user-padrino-register',
    ),
    path(
        'users/login/padrino', 
        views.LoginPadrino.as_view(),
        name='user-login-padrino',
    ),
    
    path(
        'users/perfil/padrino/', 
        views.PerfilPadrino.as_view(),
        name='user-perfil-padrino',
    ),
    
    ##Logout
    path(
        'users/logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    

   
   
  
]