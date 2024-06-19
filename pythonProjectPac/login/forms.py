from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

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
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if password != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())  # Altere para 'password'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
