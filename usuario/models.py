from django.db import models


"""criacao da classe Pessoa para armazenar dados pessoais"""
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    email =models.EmailField(blank=False, null=False)
    idade = models.CharField(max_length=3, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    bairro = models.CharField(max_length=30, blank=False, null=False)
    cidade = models.CharField(max_length=30, blank=False, null=False)
    uf = models.CharField(max_length=2, blank=False, null=False)

    """arquivo será guardado dentro da pasta fotos, no diretorio media_files"""
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)

    biografia = models.TextField(blank=True, null=True)
    senha = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nome
