from typing import List, Tuple
import pandas as pd
from collections import Counter
import re

# from memory_profiler import profile

# @profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON
    archivo = pd.read_json(file_path, lines=True)
    
    # Inicializar un contador para los emojis
    conteo_emojis = Counter()
    
    # Contar emojis en cada fila de la columna 'content'
    for mensaje in archivo['content']:
        emojis_en_mensaje = re.findall(r'[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\u2600-\u26FF\u2700-\u27BF]', mensaje)
        conteo_emojis.update(emojis_en_mensaje)
    
    # Obtener los 10 emojis más comunes
    emojis_top_10 = conteo_emojis.most_common(10)
    
    # Eliminar objetos que ya no se utilizan
    del archivo, conteo_emojis
    
    # Devolver el resultado como una lista de tuplas
    return emojis_top_10

# file_path = "C:\\Users\\jgutisal\\Downloads\\Reto\\Ejecutables\\farmers-protest-tweets-2021-2-4.json"
# q2_time(file_path)
