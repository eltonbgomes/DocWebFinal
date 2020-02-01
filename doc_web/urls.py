from django.conf.urls import url, include
from django.contrib import admin

#urls do app
urlpatterns = [
    url(r'^', include('usuario.urls')),
    url(r'^admin/', admin.site.urls),
]
