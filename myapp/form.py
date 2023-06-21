from django import forms

class formRegistro(forms.Form):
    nombre = forms.CharField(label="Nombre completo")
    correo = forms.CharField(label="Correo")
    usuario = forms.CharField(label="Usuario")
    password = forms.PasswordInput()
