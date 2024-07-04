# forms.py

from django import forms
from django.contrib.auth.hashers import make_password, check_password
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
        fields = ['entidade', 'email', 'senha', 'municipio']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")

    def save(self, commit=True):
        user = User.objects.create(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['senha'])
        )
        register = super().save(commit=False)
        register.user = user
        if commit:
            register.save()
        return register

class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput())
    entidade = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')
        entidade = cleaned_data.get('entidade')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Invalid email or password.")

        user = User.objects.get(email=email)
        if not check_password(senha, user.password):
            raise forms.ValidationError("Invalid email or password.")

        if not Register.objects.filter(user=user, entidade=entidade).exists():
            raise forms.ValidationError("Invalid entity.")

        return cleaned_data
