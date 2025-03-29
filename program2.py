import requests
from bs4 import BeautifulSoup
import random

# Función para obtener las noticias de la página principal de El País (España)
def obtener_noticias():
    url = "https://elpais.com/"
    response = requests.get(url)
    
    # Si la solicitud es exitosa
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        noticias = []
        
        # Buscar los titulares de las noticias
        for item in soup.find_all("h2", class_="headline"):
            titulo = item.get_text(strip=True)
            enlace = item.find("a")["href"]
            noticias.append((titulo, enlace))
        
        return noticias
    else:
        print("Error al acceder a la página")
        return []

# Función para recomendar noticias
def recomendar_noticia(tematica_preferida, noticias):
    # Filtrar noticias por la temática preferida
    noticias_relevantes = [noticia for noticia in noticias if tematica_preferida.lower() in noticia[0].lower()]
    
    # Si encontramos noticias relevantes, elegimos una aleatoria
    if noticias_relevantes:
        return random.choice(noticias_relevantes)
    else:
        # Si no hay noticias relacionadas, recomendar una aleatoria
        return random.choice(noticias)

# Función para simular el envío de una recomendación
def simular_notificacion(tematica, usuario):
    noticias = obtener_noticias()
    
    if noticias:
        recomendacion = recomendar_noticia(tematica, noticias)
        # Simular el mensaje de recomendación
        mensaje = (
            f"Hola {usuario},\n\n"
            f"Te recomendamos leer la siguiente noticia que podría interesarte:\n"
            f"'{recomendacion[0]}'\n\n"
            f"Puedes leerla aquí: {recomendacion[1]}"
        )
        print("\nNotificación enviada:")
        print(mensaje)
    else:
        print("No se pudieron obtener noticias para la recomendación.")

# Ejemplo de uso: Simular el envío de una notificación personalizada
usuario = "Carlos"
tematica_preferida = "economía"  # Temática de interés del usuario
simular_notificacion(tematica_preferida, usuario)
