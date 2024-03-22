from typing import List, Tuple
import re
import pandas as pd
from collections import Counter

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON
    archivo = pd.read_json(file_path, lines=True)
    
    # Inicializar un contador de emojis
    conteo_emojis = Counter()
    
    # Contar los emojis en cada fila de la columna 'content' y actualizar el contador
    for mensaje in archivo['content']:
        emojis_en_mensaje = encontrar_emojis(mensaje)
        conteo_emojis.update(emojis_en_mensaje)
    
    # Devolver los 10 emojis más comunes como una lista de tuplas
    return conteo_emojis.most_common(10)

def encontrar_emojis(mensaje):
    # Patrón de expresión regular para encontrar emojis
    patron_emojis = r'[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\u2600-\u26FF\u2700-\u27BF]'
    
    # Encuentra todos los emojis en el mensaje usando el patrón de expresión regular
    emojis_encontrados = re.findall(patron_emojis, mensaje)
    
    # Devuelve la lista de emojis encontrados
    return emojis_encontrados