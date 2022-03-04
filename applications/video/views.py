from .models import *
from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)

from applications.video.models import Video
from applications.users.mixins import EscuelaPadresPermisoMixin


class VideoListView(EscuelaPadresPermisoMixin,ListView):
    template_name = "video/list-all.html"
    context_object_name = 'videos'

    def get_queryset(self):
        return Video.objects.video_list_all()
    

    
class VideoDetail(EscuelaPadresPermisoMixin,DetailView):
    template_name='video/detail-video.html'
    
    model = Video