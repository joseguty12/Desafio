from typing import List, Tuple
import re
import pandas as pd
from collections import Counter
# from memory_profiler import profile

# @profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON
    archivo = pd.read_json(file_path, lines=True)
    
    # Inicializar un contador de emojis
    conteo_emojis = Counter()
    
    # Contar los emojis en cada fila de la columna 'content' y actualizar el contador
    for mensaje in archivo['content']:
        # Utilizar un generador para iterar sobre los emojis uno a la vez
        emojis_en_mensaje = encontrar_emojis(mensaje)
        # Actualizar el contador de emojis
        conteo_emojis.update(emojis_en_mensaje)
    
    # Devolver los 10 emojis más comunes como una lista de tuplas
    emojis_top_10 = conteo_emojis.most_common(10)
    
    # Eliminar objetos que ya no se utilizan para liberar memoria
    del archivo, conteo_emojis
    
    return emojis_top_10

def encontrar_emojis(mensaje):
    # Patrón de expresión regular para encontrar emojis
    patron_emojis = r'[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\u2600-\u26FF\u2700-\u27BF]'
    
    # Utilizar un generador para iterar sobre los emojis uno a la vez
    emojis_encontrados = re.finditer(patron_emojis, mensaje)
    
    # Devolver los emojis encontrados uno a uno
    for emoji in emojis_encontrados:
        yield emoji.group()  # Devuelve cada emoji encontrado



# Ruta del archivo JSON
# file_path = "C:\\Users\\jgutisal\\Downloads\\Reto\\Ejecutables\\farmers-protest-tweets-2021-2-4.json"

# Ejecutar la función
# q3_memory(file_path)

