## Ejercicio 01: lectura y escritura de CSV, JSON y Excel 

import os
import pandas as pd

# Tu ruta local
ruta_fichero = '/Users/jorge/Downloads/airports.csv'


def cargar_datos(ruta: str) -> pd.DataFrame:
  """Lee un fichero en formato CSV, JSON o Excel a partir de su ruta."""
  if not os.path.exists(ruta):
    raise FileNotFoundError(f'No se encontró el archivo en: {ruta}')

  ext = os.path.splitext(ruta)[-1].lower()

  if ext == '.csv':
    return pd.read_csv(ruta)
  elif ext == '.json':
    return pd.read_json(ruta)
  elif ext in ['.xlsx', '.xls']:
    return pd.read_excel(ruta)
  else:
    raise ValueError(f'Formato no soportado: {ext}')


# 1. Leemos tu archivo local
df_airports = cargar_datos(ruta_fichero)
print('Archivo cargado exitosamente. Filas y columnas:', df_airports.shape)

# 2. Exportamos a JSON y Excel en tu misma carpeta de Descargas
df_airports.to_json('/Users/jorge/Downloads/airports.json', orient='records')
df_airports.to_excel('/Users/jorge/Downloads/airports.xlsx', index=False)

# 3. Probamos leer los nuevos formatos generados
df_json = cargar_datos('/Users/jorge/Downloads/airports.json')
df_excel = cargar_datos('/Users/jorge/Downloads/airports.xlsx')