from distutils.command.upload import upload
from django.db import models
# from .managers import VideoManager

# Create your models here.
from .managers import VideoManager

class Video(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media = models.FileField(upload_to="video",blank=False)
    description = models.TextField(blank=False, null=False)
    active = models.BooleanField(default=True)
    cover_page = models.ImageField(upload_to="video/PortadaVideo" , blank=True,null=True)
    objects = VideoManager()
    
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title + '-           -' + str(self.created)
