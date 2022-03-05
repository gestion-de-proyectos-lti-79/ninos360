#
from django.urls import path

from . import views

app_name = "niño_app"

urlpatterns = [
    
    
    path(
        'users/niño/register/', 
        views.NiñoRegisterView.as_view(),
        name='user-niño-register',
    ),
    path(
        'users/login/niño', 
        views.LoginNiño.as_view(),
        name='user-login-niño',
    ),
    
    path(
        'users/perfil/niño/', 
        views.PerfilNiño.as_view(),
        name='user-perfil-niño',
    ),
    
    
    

   
   
  
]