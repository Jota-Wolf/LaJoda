from django import forms
from django.contrib.auth import get_user_model
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Cliente

class defaultForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text =' Requerido, 254 caracteres como máximo y debe ser valido')
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control mb-2 ','placeholder':''}),
            'password1': forms.PasswordInput(attrs={'class':'form-control  mb-2','placeholder':''}),
            'password2': forms.PasswordInput(attrs={'class':'form-control  mb-2','placeholder':''}),
            'email': forms.EmailInput(attrs={'class':'form-control  mb-2','placeholder':''}),
        }
        labels = {
            'username':'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Repita Contraseña',
            'email': 'Correo',
        }
    #metodo para que no se ingresen email que ya se ingresaron previamente
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro")
        return email
    
class cliForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['correo','nombre','apellido','rut','telefono']
        widgets = {
            'correo': forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':''}),
            'nombre': forms.TextInput(attrs={'class':'form-control  mb-2 required','placeholder':''}),
            'apellido': forms.TextInput(attrs={'class':'form-control  mb-2','placeholder':''}),
            'rut': forms.TextInput(attrs={'class':'form-control  mb-2','placeholder':''}),
            'telefono': forms.NumberInput(attrs={'class':'form-control  mb-2','placeholder':''}),
        }
        labels = {
            'correo': 'Repita Email',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'telefono': 'Telefono',
        }


class ClienteForm(MultiModelForm):

    form_classes = {
        'user': defaultForm,
        'cliente': cliForm, 
    }