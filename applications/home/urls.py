#
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomeView.as_view(),
        name='inicio',
    ),
    
    path(
        'no-accesso/', 
        views.NoAccesoView.as_view(),
        name='no-access',
    ),
    
]