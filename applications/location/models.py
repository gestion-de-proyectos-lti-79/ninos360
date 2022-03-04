from django.db import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey
from django.db import models

# Create your models here.
class Estado(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    
    def __str__(self):
        return self.name
    
    
    

class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        
    def __str__(self):
        return self.name
    
    

class Ubicacion(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    calle = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        
    def __str__(self):
        return self.calle
