#
from django.urls import path

from . import views

app_name = "video_app"

urlpatterns = [
    path(
        'list-video-all/', 
        views.VideoListView.as_view(),
        name='video-list-all',
    ),
    
    path(
        'video-detail/<pk>/', 
        views.VideoDetail.as_view(),
        name='video-detail',
    ),
    
]