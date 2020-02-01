from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

#Funcoes para chamar os templates


#funcao para salvar um novo cadastro e redirecionar para
#a pagina de informacoes
def cadastro_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('usuario_informacoes')


def cadastro_update(request, id):
    data  = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('usuario_informacoes')
    else:
        return render(request, 'usuario/cadastro_update.html', data)

def cadastro_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST': #somente irá deletar se vir como POST
        pessoa.delete()
        return redirect('usuario_informacoes')
    else:
        return render(request, 'usuario/delete_confirm.html', {'pessoa': pessoa})


#funcao para abrir a pagina de login
def login(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'usuario/login.html', {'pessoas': pessoas})


#funcao para abrir a pagina de cadastro
def cadastro(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'usuario/cadastro.html', data)


#funcao para abrir a pagina de informações
def informacoes(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'usuario/informacoes.html', {'pessoas': pessoas})
