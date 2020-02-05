from django.conf.urls import url, include
from .views import (
	login,
	cadastro,
	informacoes,
	cadastro_novo,
	cadastro_update,
	cadastro_delete
)

#urls das paginas do app usuario
urlpatterns = [
	url(r'^$', login, name='usuario_login'),
	url(r'^cadastro/$', cadastro, name='usuario_cadastro'),
	url(r'^informacoes/$', informacoes, name='usuario_informacoes'),

	#urls para gravar novo cadastro
	url(r'^cadastro-novo/$', cadastro_novo, name='usuario_cadastro_novo'),

	#urls para editar cadastro
	url(r'^cadastro-update/(?P<id>\d+)/$', cadastro_update, name='usuario_cadastro_update'),

	#urls para deletar cadastro
	url(r'^cadastro-delete/(?P<id>\d+)/$', cadastro_delete, name='usuario_cadastro_delete'),	
]
