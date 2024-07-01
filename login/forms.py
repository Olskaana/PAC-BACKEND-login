from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Register

class RegisterForm(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())
    MUNICIPIOS_CHOICES = [
        ('Corupá', 'Corupá'),
        ('Jaraguá do Sul', 'Jaraguá do Sul'),
        ('Schroeder', 'Schroeder'),
        ('Guaramirim', 'Guaramirim'),
        ('Masaranduba', 'Masaranduba'),
        ('São João do Itaperiu', 'São João do Itaperiu'),
        ('Barra Velha', 'Barra Velha'),
    ]
    municipio = forms.ChoiceField(choices=MUNICIPIOS_CHOICES)

    class Meta:
        model = Register
        fields = ['entidade', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.senha = make_password(self.cleaned_data['senha'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput())
    entidade = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
