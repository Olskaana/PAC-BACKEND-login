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

    def __str__(self):
        return self.subtitulo
