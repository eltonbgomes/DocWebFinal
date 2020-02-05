from django.conf.urls import url, include
from .views import home, sobre, contato


#urls das paginas do app website
urlpatterns = [
	url(r'^$', home, name='website_home'),
	url(r'^sobre$', sobre, name='website_sobre'),
	url(r'^contato$', contato, name='website_contato'),
]
