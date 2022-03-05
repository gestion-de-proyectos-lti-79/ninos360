#
from django.urls import path

from . import views

app_name = "padrino_app"

urlpatterns = [
    
    
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
    
    
    

   
   
  
]