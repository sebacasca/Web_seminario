from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class SignUpForm(ModelForm):
    direccion = forms.CharField(label = "Direccion")
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nombre")
    class Meta:
        model = User
        fields = ['username','password', 'email', 'first_name', 'last_name','direccion']
        widgets = {
            'password': forms.PasswordInput(),
        }
		
