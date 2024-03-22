from typing import List, Tuple
from datetime import datetime
import pandas as pd
# from memory_profiler import profile

# @profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Leendo el json
    archivo = pd.read_json(file_path, lines=True)
    archivo = archivo[['date', 'user']]
    
    #Convertir el campo datetime a date
    archivo['date'] = archivo['date'].dt.date
    
    # Convertir la columna de JSON en un DataFrame usando json_normalize
    df_user = pd.json_normalize(archivo['user'])
    
    # Unir el DataFrame resultante con el DataFrame original
    archivo = pd.concat([archivo,df_user],axis=1)
    
    # Eliminar la columna 'user' para liberar memoria
    del archivo['user']
    # Eliminar la columna 'user' para liberar memoria
    del df_user

    #Se identifica las top10 fechas 
    resultado = archivo.groupby('date').size().reset_index(name='conteo').sort_values(by='conteo', ascending=False)
    resultado = resultado.head(10)
    
    #Se unifica el dataframe con las top10 date con el archivo original
    archivo = pd.merge(archivo, resultado, how='inner', left_on='date', right_on='date')
    
    # Agrupar por fecha y usuario y contar los conteos
    archivo = archivo.groupby(['date', 'username']).size().reset_index(name='conteo')

    # Para cada fecha, encontrar el username con el mayor conteo
    archivo = archivo.loc[archivo.groupby('date')['conteo'].idxmax()]

    valores_tupla = [tuple(x) for x in archivo[['date', 'username']].values]
    return valores_tupla
    
# file_path = "C:\\Users\\jgutisal\\Downloads\\Reto\\Ejecutables\\farmers-protest-tweets-2021-2-4.json"
# q1_memory(file_path)
