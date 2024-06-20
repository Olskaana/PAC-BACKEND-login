from django.db import models

class Plano(models.Model):
    CATEGORIAS_CHOICES = [
        ('rio', 'Rio'),
        ('infraestrutura', 'Infraestrutura'),
        ('meio_ambiente', 'Meio Ambiente'),
        ('hidro', 'Hidro'),
    ]

    nome = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    inicio_prazo = models.DateField()
    final_prazo = models.DateField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_CHOICES)
    introducao = models.TextField()

    def __str__(self):
        return self.nome

class Topico(models.Model):
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    subtitulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='topicos/', blank=True, null=True)
    arquivo_pdf = models.FileField(upload_to='topicos/', blank=True, null=True, verbose_name='Arquivo PDF')

    def __str__(self):
        return self.subtitulo

class Adicional(models.Model):
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    subtitulo_adicional = models.CharField(max_length=100)
    texto_adicional = models.TextField()
    arquivo_pdf_adicional = models.FileField(upload_to='topicos/', blank=True, null=True, verbose_name='Arquivo PDF Adicional')
    imagem_adicional = models.ImageField(upload_to='topicos/', blank=True, null=True, verbose_name='Imagem Adicional')

    def __str__(self):
        return self.subtitulo_adicional

class Acao(models.Model):
    CATEGORIAS_ACAO_CHOICES = [
        ('acao', 'Ação'),
        ('meta', 'Meta'),
        ('diretriz', 'Diretriz'),
        ('objetivo', 'Objetivo'),
        ('recomendacao', 'Recomendação'),
    ]

    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    categoria_acao = models.CharField(max_length=50, choices=CATEGORIAS_ACAO_CHOICES)
    titulo_acao = models.CharField(max_length=100)
    descricao_acao = models.TextField()
    inicio_prazo_acao = models.DateField()
    final_prazo_acao = models.DateField()

    def __str__(self):
        return self.titulo_acao

class Biblioteca(models.Model):
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    arquivo_biblioteca = models.FileField(upload_to='biblioteca/')
    imagem_biblioteca = models.ImageField(upload_to='biblioteca/')
    url_biblioteca = models.URLField()

    def __str__(self):
        return self.arquivo_biblioteca


