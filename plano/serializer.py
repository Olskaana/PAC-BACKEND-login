from rest_framework import serializers
from .models import Plano, Topico, Adicional, Acao, Biblioteca

class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = ['nome', 'municipio', 'inicio_prazo', 'final_prazo', 'categoria', 'introducao']

class TopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topico
        fields = ['subtitulo', 'texto', 'imagem', 'arquivo_pdf']

class AdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adicional
        fields = ['subtitulo_adicional', 'texto_adicional', 'arquivo_pdf_adicional', 'imagem_adicional']

class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acao
        fields = ['categoria_acao', 'titulo_acao', 'descricao_acao', 'inicio_prazo_acao', 'final_prazo_acao']

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ['arquivo_biblioteca', 'imagem_biblioteca', 'url_biblioteca']
