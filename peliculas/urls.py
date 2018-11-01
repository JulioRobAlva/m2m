from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pelicula/nueva/$', views.pelicula_nueva, name='pelicula_nueva'),
    ]   