from typing import List, Tuple
from datetime import datetime
import pandas as pd


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer el archivo JSON
    archivo = pd.read_json(file_path, lines=True)
    archivo = archivo[['date', 'user']]
    
    # Convertir el campo datetime a date
    archivo['date'] = archivo['date'].dt.date
    
    # Convertir la columna de JSON en un DataFrame usando json_normalize
    df_user = pd.json_normalize(archivo['user'])
    
    # Unir el DataFrame resultante con el DataFrame original
    archivo = pd.concat([archivo, df_user], axis=1)
    
    # Eliminar la columna 'user' para liberar memoria
    archivo.drop(columns=['user'], inplace=True)
    
    # Identificar las top 10 fechas 
    top_fechas = archivo['date'].value_counts().nlargest(10).index
    
    # Filtrar el DataFrame original para las top 10 fechas
    df_filtrado = archivo[archivo['date'].isin(top_fechas)]
    
    # Agrupar por fecha y usuario y contar los conteos
    conteos = df_filtrado.groupby(['date', 'username']).size().reset_index(name='conteo')
    
    # Para cada fecha, encontrar el username con el mayor conteo
    usuarios_mas_frecuentes = conteos.loc[conteos.groupby('date')['conteo'].idxmax()]
    
    # Convertir a lista de tuplas
    valores_tupla = list(usuarios_mas_frecuentes[['date', 'username']].itertuples(index=False, name=None))
    
    return valores_tupla
    