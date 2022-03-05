###THIRD_PARTY_APPS
from smart_selects.db_fields import ChainedForeignKey

from django.db import models

# Create your models here.
from applications.users.models import User
from applications.location.models import Estado , Municipio


class Padrino(User):
    
    #Estado Civil
    SOLTERO = '0'
    CASADO = '1'
    SEPARADO = '2'
    DIVORCIADO = '3'
    VIUDO = '4'
    
    #Escolaridad
    PRIMARIA = '0'
    SECUNDARIA = '1'
    PREPARATORIA = '2'
    TECNICA = '3'
    PROFESIONAL= '4'
    MAESTRIA= '5'
    DOCTORADO= '6'
    
    
    ESCOLARIDAD_CHOICES = [
        (PRIMARIA, 'Primaria'),
        (SECUNDARIA, 'Secundaria'),
        (PREPARATORIA, 'Preparatoria'),
        (TECNICA, 'Tecnica'),
        (PROFESIONAL, 'Profesional'),
        (TECNICA, 'Maestria'),
        (DOCTORADO, 'Doctorado'),
    ]
    
    ESTADOCIVIL_CHOICES = [
        (SOLTERO, 'Soltero'),
        (CASADO, 'Casado/a'),
        (SEPARADO, 'Separado/a'),
        (DIVORCIADO, 'Divorciado/a'),
        (VIUDO, 'Viudo/a')
    ]
    
    estadoCivil = models.CharField(
        max_length=1, 
        choices=ESTADOCIVIL_CHOICES, 
        blank=True,
        null=True
    )
    
    escolaridad = models.CharField(
        max_length=1, 
        choices=ESCOLARIDAD_CHOICES, 
        blank=True,
        null=True
    )
    
    phoneNumber = models.CharField(unique = True, max_length=20, null = True, blank = True) 
    
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True
    )
    
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
        
    )
    
    class Meta:
        verbose_name = 'Padrino'
        verbose_name_plural = 'Padrinos'