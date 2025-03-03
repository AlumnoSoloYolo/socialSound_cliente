import requests
from django.conf import settings
import base64
import json
from django.contrib import messages


# def crear_cabecera():
#     return {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}

class helper:
    
    def obtener_token_session(usuario, password):
        token_url = f'{settings.API_BASE_URL}oauth2/token/'
        print(f"URL de token: {token_url}")
        
        data = {
            'grant_type': 'password',
            'username': usuario,
            'password': password,
            'client_id': 'mi_aplicacion',  # Ajusta según tu configuración
            'client_secret': 'mi_clave_secreta',  # Ajusta según tu configuración
        }
        
        print(f"Datos para obtener token: {json.dumps(data)}")
        
        try:
            response = requests.post(token_url, data=data)
            print(f"Código de respuesta token: {response.status_code}")
            print(f"Respuesta token: {response.text[:100]}...")
            
            if response.status_code == 200:
                respuesta = response.json()
                token = respuesta.get('access_token')
                if token:
                    return token
                else:
                    raise Exception("No se recibió un token de acceso en la respuesta")
            else:
                # Intentar obtener mensaje de error
                try:
                    respuesta = response.json()
                    error_msg = respuesta.get("error_description", "Error desconocido")
                except json.JSONDecodeError:
                    error_msg = response.text or "Error desconocido"
                
                raise Exception(f"Error al obtener token ({response.status_code}): {error_msg}")
        
        except requests.RequestException as e:
            raise Exception(f"Error de conexión: {str(e)}")
        except json.JSONDecodeError:
            raise Exception(f"Error al procesar respuesta: formato inválido")
        except Exception as e:
            raise Exception(f"Error inesperado: {str(e)}")
        

    def obtener_usuario(usuario_id):
        headers = {'Authorization': f'Token {settings.AUTH_TOKEN}'} 
        response = requests.get(f'{settings.API_URL}usuarios/{str(usuario_id)}', headers=headers)
        usuario = response.json()
        return usuario

     
    def validar_nombre_usuario_existe(nombre_usuario):
        """Valida si un nombre de usuario ya existe"""
        try:
            headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
            response = requests.get(
                f'{settings.API_URL}usuarios/validar-nombre/{nombre_usuario}',
                headers=headers
            )
            return response.status_code == 200
        except:
            return False

    
    def validar_email_existe(email):
        """Valida si un email ya existe"""
        try:
            headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
            response = requests.get(
                f'{settings.API_URL}usuarios/validar-email/{email}',
                headers=headers
            )
            return response.status_code == 200
        except:
            return False

    
    def validar_like_existe(usuario_id, cancion_id):
        """Valida si ya existe un like para una canción de un usuario"""
        try:
            headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
            response = requests.get(
                f'{settings.API_URL}likes/validar/{usuario_id}/{cancion_id}',
                headers=headers
            )
            return response.status_code == 200
        except:
            return False
    

    def obtener_albumes_select():
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
        response = requests.get(f'{settings.API_URL}albumes/', headers=headers)
        albumes = response.json()
        
        lista_albumes = [("", "Seleccione un álbum")]
        for album in albumes:
            lista_albumes.append((album["id"], album["titulo"]))
        return lista_albumes
    

    def obtener_usuarios_select():
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
        response = requests.get(f'{settings.API_URL}usuarios/', headers=headers)
        usuarios = response.json()
        
        lista_usuarios = [("", "Seleccione un usuario")]
        for usuario in usuarios:
            lista_usuarios.append((usuario["id"], usuario["nombre_usuario"]))
        return lista_usuarios
    
    def obtener_album(id):
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
        response = requests.get(f'{settings.API_URL}albumes/{id}/', headers=headers)
        if response.status_code == 200:
            return response.json()
        raise Exception(f"Error al obtener álbum: {response.text}")
    
 

    def obtener_detalle_album(id):
        print("Iniciando obtener_detalle_album")
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
        
     
        response = requests.get(f'{settings.API_URL}albumes/detalles/{id}', headers=headers)
      
        return response.json()
    
    def obtener_canciones_select():
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'} 
        response = requests.get(f'{settings.API_URL}canciones', headers=headers)
        canciones = response.json()
        
        lista_canciones = []
        for cancion in canciones:
            lista_canciones.append((cancion["id"], f"{cancion['titulo']} - {cancion['artista']}"))
        return lista_canciones

    def obtener_playlist(id):
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'} 
        response = requests.get(f'{settings.API_URL}playlists/{id}', headers=headers)
        return response.json()

    def obtener_playlists_select():
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
        response = requests.get(f'{settings.API_URL}playlists/', headers=headers)
        playlists = response.json()
        
        lista_playlists = [("", "Seleccione una playlist")]
        for playlist in playlists:
            lista_playlists.append((playlist["id"], playlist["nombre"]))
        return lista_playlists


    def obtener_canciones_playlist(playlist_id):
        headers = {'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}'}
        response = requests.get(f'{settings.API_URL}playlists/{playlist_id}/', headers=headers)
        playlist = response.json()
        return [cancion.get(id) for cancion in playlist.get('canciones', [])]
    

    def crear_cabecera_contentType():
        return {
            'Authorization': f'Bearer {settings.OAUTH_TOKENS[1]}',
            'Content-Type': 'application/json'
        }

    def procesar_imagen(imagen):
     
        if not imagen:
            return None
        with imagen.open('rb') as file:
            contenido = file.read()
        encoded = base64.b64encode(contenido).decode('utf-8')
        return f"data:{imagen.content_type};base64,{encoded}"

    def manejar_respuesta_api(response, mensaje_exito=None, request=None):
     
        if response.status_code in [200, 201]:
            if mensaje_exito and request:
                messages.success(request, mensaje_exito)
            return True, None
        return False, response.status_code

    def manejar_errores_formulario(response, formulario):
      
        if response.status_code == 400:
            errores = response.json()
            for campo, mensaje in errores.items():
                formulario.add_error(campo, mensaje)
        return formulario

    def realizar_peticion_crear(url, datos, files=None):
        try:
            headers = helper.crear_cabecera_contentType()
            
           
            print(f"URL: {settings.API_URL}{url}")
            print(f"Headers: {headers}")
            print(f"Datos a enviar: {json.dumps(datos)[:500]}")  
            
            response = requests.post(
                f'{settings.API_URL}{url}',
                headers=headers,
                data=json.dumps(datos)
            )
      
            print(f"Status Code: {response.status_code}")
            try:
                print(f"Response: {response.json()}")
            except:
                print(f"Response texto: {response.text[:500]}")
                
            return response
            
        except Exception as e:
            print(f"Error en realizar_peticion_crear: {e}")
            raise
    

    def realizar_peticion_actualizar(url, datos, files=None, method='PUT'):
        
        headers = helper.crear_cabecera_contentType()
        
        if files:
            for key, file in files.items():
                if file:
                    datos[key] = helper.procesar_imagen(file)
                elif key in datos:
                    datos.pop(key)

        request_method = requests.put if method == 'PUT' else requests.patch
        return request_method(
            f'{settings.API_URL}{url}',
            headers=headers,
            data=json.dumps(datos)
        )

    def realizar_peticion_eliminar(url):
   
        headers = helper.crear_cabecera_contentType()
        return requests.delete(
            f'{settings.API_URL}{url}',
            headers=headers
        )