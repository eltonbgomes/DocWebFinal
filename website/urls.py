from django.conf.urls import url, include
from .views import home


#urls das paginas do app website
urlpatterns = [
	url(r'^$', home, name='website_home'),	
]
