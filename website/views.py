from django.shortcuts import render
from .models import Contato


def home(request):
	return render(request, 'website/index.html')


def sobre(request):
	return render(request, 'website/sobre.html')


def contato(request):
	mensagem = ''
	#teste logico para impedir mensagem de vazio no template
	if request.method == 'POST':
		try:
			contato = {}
			contato['email'] = request.POST.get('email')
			contato['nome'] = request.POST.get('nome')
			contato['sobrenome'] = request.POST.get('sobrenome')
			contato['endereco'] = request.POST.get('endereco')
			contato['cidade'] = request.POST.get('cidade')
			contato['estado'] = request.POST.get('estado')
			contato['mensagem'] = request.POST.get('mensagem')
			contato['receber_noticias'] = True if request.POST.get('receber_noticias') == 'on' else False
		
			Contato.objects.create(**contato) #Coloca todas as variaveis do dicio no objeto

		except Exception as erro:
			mensagem = str(erro)
		else:
			mensagem = 'Contato realizado com sucesso.'

	return render(request, 'website/contato.html', {'mensagem': mensagem})
