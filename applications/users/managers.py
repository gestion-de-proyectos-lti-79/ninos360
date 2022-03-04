from django.db import models
#
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    ###Escuela Padres
    def _create_user_Escuela_Padres(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    
    ##Padrino
    def _create_user_Padrino(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    ##Terminal
    def _create_userTerminal(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            ocupation='0',
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    
    
    def create_userEscuelaPadres(self, email, password=None, **extra_fields):
        return self._create_user_Escuela_Padres(email, password, False, False, True, **extra_fields)
    
    
    def create_userPadrino(self, email, password=None, **extra_fields):
        return self._create_user_Padrino(email, password, False, False, True, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_userTerminal(email, password, True, True, True, **extra_fields)
    
        

    
    
    
    
    

    
    