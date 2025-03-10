from django.urls import path
from .views import *



urlpatterns = [
     path('', index, name="index"),
     path('playlists/', lista_playlists_api, name='lista_playlists'),
     path('albumes/', lista_albumes_api, name='lista_albumes'),
     # path('usuarios/<str:nombre_usuario>/albumes/', lista_albumes_usuario_api, name='lista_albumes_usuario'),
     path('usuarios/lista_usuarios_completa/', lista_usuarios_completa_api, name="lista_usuarios_completa"),
     path('canciones/', lista_canciones_api, name='lista_canciones'),
     path('canciones/generos/', canciones_por_genero_api, name='canciones_por_genero_api'),
     path('usuarios/busqueda_usuarios', busqueda_usuarios_api, name='busqueda_usuarios'),
     path('usuarios/busqueda_avanzada/', usuario_busqueda_avanzada_api, name='usuarios_busqueda_avanzada'),
     path('albumes/busqueda_avanzada/', album_busqueda_avanzada_api, name='albumes_busqueda_avanzada'),
     path('canciones/busqueda_avanzada/', cancion_busqueda_avanzada_api, name='canciones_busqueda_avanzada'),
     path('playlists/busqueda_avanzada/', playlist_busqueda_avanzada_api, name='playlists_busqueda_avanzada'),

     path('usuario/crear/', usuario_crear, name='usuario_crear'),
     path('usuario/editar/<int:id>', usuario_editar, name='usuario_editar'),
     path('usuario/editar/nombre/<int:usuario_id>', usuario_editar_nombre, name='usuario_editar_nombre'),
     path('usuario/eliminar/<int:usuario_id>', usuario_eliminar, name='usuario_eliminar'),

     path('albumes/crear/', album_crear, name='album_crear'),
     path('albumes/editar/<int:id>/', album_editar, name='album_editar'),
     path('albumes/editar-titulo/<int:id>/', album_editar_titulo, name='album_editar_titulo'),
     path('albumes/eliminar/<int:id>/', album_eliminar, name='album_eliminar'),

     path('playlists/crear/', playlist_crear, name='playlist_crear'),
     path('playlists/<int:id>/editar/', playlist_editar, name='playlist_editar'),
     path('playlists/<int:id>/editar/canciones/', playlist_editar_canciones, name='playlist_editar_canciones'),
     path('playlists/eliminar/<int:id>/', playlist_eliminar, name='playlist_eliminar'),

     path('likes/crear/', like_crear, name='like_crear'),
     path('likes/eliminar/', like_eliminar, name='like_eliminar'),

     path('cancion-playlist/crear/', cancion_playlist_crear, name='cancion_playlist_crear'),
     path('cancion-playlist/<int:id>/editar/', cancion_playlist_editar, name='cancion_playlist_editar'),
     path('detalles-album/crear/', detalle_album_crear, name='detalle_album_crear'),
     path('detalles-album/editar/<int:id>/', detalle_album_editar, name='detalle_album_editar'),

     path('registrar/', registrar_usuario, name='registrar'),
     path('login/', login_usuario, name='login'),
     path('logout/', logout, name='logout'),

     path('perfil/', perfil_usuario, name='perfil_usuario'),
     path('perfil/<int:usuario_id>/', perfil_usuario, name='perfil_usuario_detalle'),
     path('usuario/<str:nombre_usuario>/albumes/', albumes_usuario, name='albumes_usuario'),

     path('cancion/<int:cancion_id>/like/', dar_like, name='dar_like'),
     path('cancion/<int:cancion_id>/unlike/', quitar_like, name='quitar_like'),

     path('usuario/<int:usuario_id>/seguir/', seguir, name='seguir_usuario'),
     path('usuario/<int:usuario_id>/dejar-seguir/', dejar_seguir, name='dejar_seguir_usuario'),

     path('cors-prueba/', cors_prueba, name='cors_prueba'),

]
