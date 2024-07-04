import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from plano.models import Plano, Topico, Adicional, Acao, Biblioteca

@pytest.fixture
def db_setup(django_db_setup):
    User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def plano_form_data():
    return {
        'nome': 'Novo Plano',
        'inicio_prazo': timezone.now().date(),
        'final_prazo': timezone.now().date(),
        'categoria': 'rio',
        'introducao': 'Introdução do novo plano',
    }

@pytest.fixture
def topico_form_data():
    return {
        'titulo': 'Novo Tópico',
        'conteudo': 'Conteúdo do novo tópico',
    }

@pytest.fixture
def adicional_form_data():
    return {
        'subtitulo_adicional': 'Novo Subtítulo Adicional',
        'texto_adicional': 'Texto do novo adicional',
    }

@pytest.fixture
def acao_form_data():
    return {
        'categoria_acao': 'acao',
        'titulo_acao': 'Novo Título Ação',
        'descricao_acao': 'Descrição da nova ação',
        'inicio_prazo_acao': timezone.now().date(),
        'final_prazo_acao': timezone.now().date(),
    }

@pytest.fixture
def biblioteca_form_data():
    return {
        'url_biblioteca': 'http://teste.com',
    }

@pytest.fixture
def arquivo_biblioteca():
    from django.core.files.uploadedfile import SimpleUploadedFile
    return SimpleUploadedFile("livro.pdf", b"conteudo do arquivo", content_type="application/pdf")

@pytest.fixture
def imagem_biblioteca():
    from django.core.files.uploadedfile import SimpleUploadedFile
    return SimpleUploadedFile("imagem.jpg", b"conteudo da imagem", content_type="image/jpeg")


@pytest.fixture
def plano(db_setup):
    return Plano.objects.create(
        nome='Plano de Teste',
        inicio_prazo=timezone.now().date(),
        final_prazo=timezone.now().date() + timezone.timedelta(days=30),
        categoria='rio',
        introducao='Introdução do plano de teste'
    )
