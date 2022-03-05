from django import forms
from .models import Padrino
from django.contrib.auth import authenticate, login, logout








class PadrinoRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'input-group-field',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'input-group-field',
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = Padrino
        fields = (
            'first_name',
            'last_name',
            'email',
            'genero',
            'date_birth',
            'estado',
            'municipio',
            'phoneNumber',
            'estadoCivil',
            'escolaridad'
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-group-field',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre ...',
                    'class': 'input-group-field',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido ...',
                    'class': 'input-group-field',
                }
            ),
            'date_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs = {
                    'type': 'date',
                    'class': 'input-group-field',
                }
            )
            
            
            
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')




class PadrinoLoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'Correo Electronico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(PadrinoLoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data