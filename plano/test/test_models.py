import pytest
from django.utils import timezone
from django.core.exceptions import ValidationError
from plano.models import Plano, Topico, Adicional, Acao, Biblioteca

@pytest.mark.django_db
class TestPlanoModel:
    @pytest.mark.parametrize(
        "nome, municipio, categoria, introducao, expected",
        [
            ("Plano 1", "Cidade 1", "rio", "Introdução 1", True),
            ("Plano 2", "Cidade 2", "infraestrutura", "Introdução 2", True),
            ("Plano 3", "Cidade 3", "meio_ambiente", "Introdução 3", True),
            ("Plano 4", "Cidade 4", "categoria_invalida", "Introdução 4", False),
        ]
    )
    def test_create_plano_parametrize(self, nome, municipio, categoria, introducao, expected):
        if expected:
            plano = Plano(
                nome=nome,
                municipio=municipio,
                inicio_prazo=timezone.now().date(),
                final_prazo=timezone.now().date() + timezone.timedelta(days=30),
                categoria=categoria,
                introducao=introducao
            )
            plano.full_clean()
            plano.save()
            assert plano.nome == nome
            assert str(plano) == nome
        else:
            with pytest.raises(ValidationError):
                plano = Plano(
                    nome=nome,
                    municipio=municipio,
                    inicio_prazo=timezone.now().date(),
                    final_prazo=timezone.now().date() + timezone.timedelta(days=30),
                    categoria=categoria,
                    introducao=introducao
                )
                plano.full_clean()

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

@pytest.mark.django_db
class TestTopicoModel:
    def test_create_topico(self, plano):
        topico = Topico.objects.create(
            plano=plano,
            subtitulo="Subtítulo Teste",
            texto="Texto do tópico teste"
        )
        assert topico.subtitulo == "Subtítulo Teste"
        assert str(topico) == "Subtítulo Teste"

@pytest.mark.django_db
class TestAdicionalModel:
    def test_create_adicional(self, plano):
        adicional = Adicional.objects.create(
            plano=plano,
            subtitulo_adicional="Subtítulo Adicional Teste",
            texto_adicional="Texto adicional teste"
        )
        assert adicional.subtitulo_adicional == "Subtítulo Adicional Teste"
        assert str(adicional) == "Subtítulo Adicional Teste"

@pytest.mark.django_db
class TestAcaoModel:
    def test_create_acao(self, plano):
        acao = Acao.objects.create(
            plano=plano,
            categoria_acao="acao",
            titulo_acao="Título Ação Teste",
            descricao_acao="Descrição da ação teste",
            inicio_prazo_acao=timezone.now().date(),
            final_prazo_acao=timezone.now().date() + timezone.timedelta(days=10)
        )
        assert acao.titulo_acao == "Título Ação Teste"
        assert str(acao) == "Título Ação Teste"

@pytest.mark.django_db
class TestBibliotecaModel:
    def test_create_biblioteca(self, plano):
        biblioteca = Biblioteca.objects.create(
            plano=plano,
            arquivo_biblioteca="arquivo_teste.pdf",
            imagem_biblioteca="imagem_teste.jpg",
            url_biblioteca="http://teste.com"
        )
        assert biblioteca.url_biblioteca == "http://teste.com"
        assert str(biblioteca) == "arquivo_teste.pdf"

@pytest.fixture
def plano(db):
    return Plano.objects.create(
        nome="Plano Fixture",
        municipio="Fixture",
        inicio_prazo=timezone.now().date(),
        final_prazo=timezone.now().date() + timezone.timedelta(days=30),
        categoria="rio",
        introducao="Introdução do plano fixture"
    )
