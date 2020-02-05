from django.db import models


#classe contato para armazenar os contatos da pagina contato
class Contato(models.Model):
	email = models.EmailField(max_length=100)
	nome = models.CharField(max_length=100)
	sobrenome = models.CharField(max_length=100)
	endereco = models.CharField(max_length=100)
	cidade = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	mensagem = models.TextField()
	receber_noticias = models.BooleanField()

	def __str__(self):
		return self.nome
