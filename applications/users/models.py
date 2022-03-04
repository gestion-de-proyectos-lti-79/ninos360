from tabnanny import verbose
from smart_selects.db_fields import ChainedForeignKey

from django.db import models

# Create your models here.
from applications.location.models import Estado, Municipio
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager


###############################  ESCUELA PADRES ######################################################
class User(AbstractBaseUser, PermissionsMixin):
    # TIPO DE USUARIOS
    ADMINISTRADOR = '0'
    PADRE = '1'
    NIÑO = '2'
    PADRINO = '3'
    # GENEROS
    VARON = 'M'
    MUJER = 'F'
    OTRO = 'O'
    #
    OCUPATION_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (PADRE, 'Padre'),
        (NIÑO, 'Niño'),
        (PADRINO, 'Padrino'),
    ]

    GENDER_CHOICES = [
        (VARON, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField('Nombre', max_length=100, null=True)
    last_name = models.CharField('Apellido', max_length=50, null=True)
    ocupation = models.CharField(
        max_length=1, 
        choices=OCUPATION_CHOICES, 
        blank=True
    )
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    def get_first_name(self):
        return self.first_name


class Padrino(User):
    
    phoneNumber = models.CharField(unique = True, max_length=20, null = True, blank = True) 
    
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'Padrino'
        verbose_name_plural = 'Padrinos'
    
    
    
# class Niño(Padrino):
    
#     #Escolaridad
#     PRIMARIA = '0'
#     SECUNDARIA = '1'
#     PREPARATORIA = '2'
#     TECNICA = '3'
#     PROFESIONAL= '4'
#     MAESTRIA= '5'
#     DOCTORADO= '6'
    
    
#     ESCOLARIDAD_CHOICES = [
#         (PRIMARIA, 'Primaria'),
#         (SECUNDARIA, 'Secundaria'),
#         (PREPARATORIA, 'Preparatoria'),
#         (TECNICA, 'Tecnica'),
#         (PROFESIONAL, 'Profesional'),
#         (TECNICA, 'Maestria'),
#         (DOCTORADO, 'Doctorado'),
#     ]
