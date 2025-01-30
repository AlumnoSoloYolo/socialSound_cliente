from django.urls import path
from .views import *



urlpatterns = [
     path('playlists/', lista_playlists_api, name='lista_playlists'),
     path('usuarios/<str:nombre_usuario>/albumes/', lista_albumes_usuario_api, name='lista_albumes_usuario'),
     path('usuarios/lista_usuarios_completa/', lista_usuarios_completa_api, name="lista_usuarios_completa"),
     path('canciones/', lista_canciones_api, name='lista_canciones'),
     path('canciones/generos/', canciones_por_genero_api, name='canciones_por_genero_api')

]
