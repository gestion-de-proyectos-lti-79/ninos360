from django.db import models

from applications.padrino.models import Padrino


# Create your models here.


class Niño(Padrino):
    
    escuela = models.CharField(max_length=150, blank=False, null=False)
    kardex = models.FileField(upload_to="kardex",blank=False, null=False)
    
    class Meta:
        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'