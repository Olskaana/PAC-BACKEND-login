from django.db import models

class Register(models.Model):
    entidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email
