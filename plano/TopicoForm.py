from django import forms
from .models import Topico

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['subtitulo', 'texto', 'imagem', 'arquivo_pdf']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arquivo_pdf'].widget.attrs['accept'] = '.pdf'  # Limita a seleção de arquivos a PDFs