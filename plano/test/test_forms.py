import pytest
from django.utils import timezone
from ..forms import PlanoForm, TopicoForm, AdicionalForm, BibliotecaForm, AcaoForm
from django.core.files.uploadedfile import SimpleUploadedFile
import os

@pytest.mark.django_db
class TestTopicoForm:
    @pytest.fixture
    def topico_form_data(self):
        return {
            'plano': None,  # Inserir o ID do plano aqui se necessário
            'subtitulo': 'Subtítulo do Tópico',
            'texto': 'Texto do Tópico'
        }

    def test_topico_form(self, topico_form_data):
        form = TopicoForm(data=topico_form_data)
        assert form.is_valid() is True
 
@pytest.mark.django_db     
def test_biblioteca_form(plano, arquivo_biblioteca, imagem_biblioteca):
    form_data = {
        'plano': plano.id,
        'url_biblioteca': 'http://teste.com',
    }

    file_data = {
        'livro_2.pdf': arquivo_biblioteca,
        'jpeg.jpeg': imagem_biblioteca,
    }

    form = BibliotecaForm(data=form_data, files=file_data)

    assert form.is_valid(), f"Formulário inválido: {form.errors.as_data()}"
    
    
@pytest.mark.django_db
class TestAcaoForm:
    @pytest.fixture
    def acao_form_data(self):
        return {
            'categoria_acao': 'acao',
            'titulo_acao': 'Título Ação Teste',
            'descricao_acao': 'Descrição da ação teste',
            'inicio_prazo_acao': timezone.now().date(),
            'final_prazo_acao': timezone.now().date() + timezone.timedelta(days=10)
        }

    def test_acao_form(self, plano, acao_form_data):
        form = AcaoForm(data={
            'plano': plano.id,
            **acao_form_data
        })
        assert form.is_valid() is True
        
@pytest.mark.django_db
class TestAdicionalForm:
    @pytest.fixture
    def adicional_form_data(self):
        return {
            'subtitulo_adicional': 'Subtítulo Adicional Teste',
            'texto_adicional': 'Texto adicional teste'
        }

    def test_adicional_form(self, plano, adicional_form_data):
        form = AdicionalForm(data={
            'plano': plano.id,
            **adicional_form_data
        })
        assert form.is_valid(), f"Formulário inválido: {form.errors.as_data()}"

        # Exemplo de verificação adicional (opcional)
        assert form.cleaned_data['subtitulo_adicional'] == adicional_form_data['subtitulo_adicional']
        assert form.cleaned_data['texto_adicional'] == adicional_form_data['texto_adicional']
        
