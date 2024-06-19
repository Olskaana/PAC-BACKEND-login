# forms.py
from django import forms
from .models import Plano, Topico

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'inicio_prazo', 'final_prazo', 'categoria', 'introducao']

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['subtitulo', 'texto', 'imagem']
