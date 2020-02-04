from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

#urls do app
urlpatterns = [
    url(r'^', include('website.urls')),
    url(r'^sistema/', include('usuario.urls')),
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
