# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

class FormaContacto(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), required=True)
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'class': 'form-control'}), required=True)


class FormaSuscripcion(forms.Form):
    email_suscripcion = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico', 'class': 'form-control'}), required=True) 