from django import forms
from .models import Plano, Topico, Adicional, Biblioteca, Acao

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'inicio_prazo', 'final_prazo', 'categoria', 'introducao']

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['subtitulo', 'texto', 'imagem', 'arquivo_pdf']

class TopicoFileForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['arquivo_pdf']

class TopicoImageForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['imagem']

class AdicionalForm(forms.ModelForm):
    class Meta:
        model = Adicional
        fields = ['subtitulo_adicional', 'texto_adicional', 'arquivo_pdf_adicional', 'imagem_adicional']

class AdicionalFileForm(forms.ModelForm):
    class Meta:
        model = Adicional
        fields = ['arquivo_pdf_adicional']

class AdicionalImageForm(forms.ModelForm):
    class Meta:
        model = Adicional
        fields = ['imagem_adicional']

class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['arquivo_biblioteca', 'imagem_biblioteca', 'url_biblioteca']

class BibliotecaFileForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['arquivo_biblioteca']

class BibliotecaImageForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['imagem_biblioteca']

class AcaoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = ['categoria_acao', 'titulo_acao', 'descricao_acao', 'inicio_prazo_acao', 'final_prazo_acao']

