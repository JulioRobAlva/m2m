from django.contrib import admin
from peliculas.models import Actor, ActorAdmin, Pelicula, PeliculaAdmin

admin.site.register(Actor, ActorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)