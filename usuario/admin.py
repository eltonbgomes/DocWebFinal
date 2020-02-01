from django.contrib import admin
from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'cidade', 'email')


admin.site.register(Pessoa, PessoaAdmin)
