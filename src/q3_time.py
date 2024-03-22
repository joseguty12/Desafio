import pandas as pd
from collections import Counter
from typing import List, Tuple
# from memory_profiler import profile

# @profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON
    archivo = pd.read_json(file_path, lines=True)
    
    # Contar la frecuencia de cada username en todas las filas
    conteo_usernames = Counter(username for usernames_list in archivo['mentionedUsers'] for username in obtener_username(usernames_list))

    # Obtener los 10 usernames más frecuentes
    usernames_top_10 = conteo_usernames.most_common(10)

    # Eliminar objetos que ya no necesitamos
    del archivo
    del conteo_usernames
    
    return usernames_top_10

# Función para obtener usernames de una lista
def obtener_username(lista):
    if lista:
        return [usuario['username'] for usuario in lista]
    else:
        return []  # Devolver una lista vacía si la lista de usuarios está vacía

# file_path = "C:\\Users\\jgutisal\\Downloads\\Reto\\Ejecutables\\farmers-protest-tweets-2021-2-4.json"
# q3_time(file_path)