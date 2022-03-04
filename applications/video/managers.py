from pyexpat import model
from django.db import models



class VideoManager(models.Manager):
    
    
    
    def video_list_all(self):
        return self.filter(
            active=True
        ).order_by('-created')