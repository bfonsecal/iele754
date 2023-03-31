import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


url='https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'

df = pd.read_csv(url)


#Se seleccionan las columnas que tienen fechas
vals= list(df.columns)[5:-1]
#Se seleccionan el resto de las columnas
ids= list(df.columns)[:5]

df_tidy= pd.melt(df, value_vars=vals, id_vars=ids)

df_tidy= df_tidy.rename(columns={'variable':'fechas'})

df_tidy['fechas']=pd.to_datetime(df_tidy['fechas'], format='%d-%m-%Y')

#En formato date time y nombre fechas
#Se borran N/a y columnas irrelevantes
df_tidy.dropna(inplace=True)
df_tidy = df_tidy.drop(['Codigo region', 'Codigo comuna'], axis=1)
df_tidy = df_tidy[(df_tidy["fechas"].dt.month >= 3) & (df_tidy["fechas"].dt.month <= 6) & (df_tidy["fechas"].dt.year == 2020)]

df_tidy['Casos Nuevos'] = df_tidy.groupby('Comuna')['value'].diff()

# Agrupa los datos por fecha y suma los casos nuevos de todas las comunas
df_fecha = df_tidy.groupby('fechas')['Casos Nuevos'].sum().reset_index()

# Crea una gráfica de línea
plt.plot(df_fecha['fechas'], df_fecha['Casos Nuevos'])

# Agrega etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Casos Nuevos')
plt.title('Casos Nuevos de COVID-19')

# Muestra la gráfica
plt.show()