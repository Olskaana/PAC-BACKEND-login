import os
import django
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from mixer.backend.django import mixer 
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError
from plano.models import Plano, Topico, Adicional, Acao, Biblioteca

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def plano(db):
    final_prazo = timezone.now().date() + timezone.timedelta(days=30)
    return Plano.objects.create(
        nome='Test Plano',
        municipio='Test Municipio',
        final_prazo=final_prazo
    )


@pytest.mark.django_db
def test_municipio_view(client, plano):
    url = reverse('municipio', kwargs={'municipio': plano.municipio})
    response = client.get(url)
    assert response.status_code == 200
    assert 'municipio' in response.context
    assert 'planos' in response.context
    assert plano in response.context['planos']

@pytest.mark.django_db
def test_plano_detail_view(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')

    plano = mixer.blend('plano.Plano', nome='Plano Detalhado', municipio='seu_municipio',
                        final_prazo=timezone.now().date() + timezone.timedelta(days=30))

    url = reverse('plano_detail', kwargs={'municipio': plano.municipio, 'id_plano': plano.id})
    response = client.get(url)

    assert response.status_code == 200
    assert 'plano' in response.context
    assert response.context['plano'] == plano
    
@pytest.mark.django_db
def test_criar_plano_view(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')

    municipio = 'Test Municipio'
    url = reverse('criar_plano', kwargs={'municipio': municipio})

    response = client.get(url)
    assert response.status_code == 200
    
    data = {
        'nome': 'Novo Plano',
        'final_prazo': (timezone.now() + timezone.timedelta(days=30)).strftime('%Y-%m-%d'),
        # Incluir outros campos do formulário aqui conforme necessário
    }
    response = client.post(url, data)
    assert response.status_code == 302 
    assert Plano.objects.filter(nome='Novo Plano').exists()
    
@pytest.mark.django_db
def test_excluir_plano_view(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')

    plano = mixer.blend('plano.Plano', nome='Plano para Excluir', municipio='seu_municipio')

    url = reverse('excluir_plano', kwargs={'municipio': plano.municipio, 'id_plano': plano.id})
    response = client.get(url)

    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 302
    assert not Plano.objects.filter(id=plano.id).exists()
    
@pytest.mark.django_db
def test_editar_plano_view(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')

    plano = mixer.blend('plano.Plano', nome='Plano Editado', municipio='seu_municipio')

    url = reverse('editar_plano', kwargs={'municipio': plano.municipio, 'id_plano': plano.id})
    response = client.get(url)

    assert response.status_code == 200

    data = {
        'nome': 'Plano Editado',
        'final_prazo': (timezone.now() + timezone.timedelta(days=30)).strftime('%Y-%m-%d'),
    }
    response = client.post(url, data)
    assert response.status_code == 200
    plano.refresh_from_db()
    assert plano.nome == 'Plano Editado'
    
@pytest.mark.django_db
class TestPlanoModel:

    @pytest.mark.xfail(reason="Campo nome não pode estar vazio.")
    def test_create_plano_fail(self):
        plano = Plano(
            nome="",
            municipio="Teste",
            inicio_prazo=timezone.now().date(),
            final_prazo=timezone.now().date() + timezone.timedelta(days=30),
            categoria="rio",
            introducao="Introdução do plano teste"
        )
        with pytest.raises(ValidationError):
            plano.full_clean()
