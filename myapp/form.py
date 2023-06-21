<<<<<<< HEAD
from django import forms

class formRegistro(forms.Form):
    nombre = forms.CharField(label="Nombre completo")
    correo = forms.CharField(label="Correo")
    usuario = forms.CharField(label="Usuario")
    password = forms.PasswordInput()
=======
from django import forms

class formRegistro(forms.Form):
    nombre = forms.CharField(label="Nombre completo")
    correo = forms.CharField(label="Correo")
    usuario = forms.CharField(label="Usuario")
    password = forms.PasswordInput()
>>>>>>> adea497916b6fbb42bf4fdedd9214626e0f16cf5
