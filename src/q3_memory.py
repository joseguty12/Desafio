from typing import List, Tuple
import pandas as pd
# from memory_profiler import profile
from collections import Counter

# @profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON
    archivo = pd.read_json(file_path, lines=True)

    # Aplicar una función para obtener los usernames de cada lista
    usernames_series = archivo['mentionedUsers'].apply(obtener_username)

    # Contar la frecuencia de cada username
    conteo_usernames = Counter(username for usernames_list in archivo['mentionedUsers'].apply(obtener_username) for username in usernames_list)

    # Obtener los 10 usernames más frecuentes
    usernames_top_10 = conteo_usernames.most_common(10)

    # Eliminar objetos que ya no necesitamos
    del archivo
    del usernames_series
    del conteo_usernames
    
    return usernames_top_10
    
def obtener_username(lista):
    if lista:  # Verificar si la lista no está vacía
        return [usuario['username'] for usuario in lista] # Obtener el username si existe, o devolver una lista vacía si la lista está vacía
    else:
        return []  # Devolver una lista vacía si la lista está vacía


# Ruta del archivo JSON
# file_path = "C:\\Users\\jgutisal\\Downloads\\Reto\\Ejecutables\\farmers-protest-tweets-2021-2-4.json"

# Ejecutar la función
# q3_memory(file_path)


