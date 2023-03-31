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
#Seleccionamos solo de marzo a junio
df_tidy = df_tidy[(df_tidy["fechas"].dt.month >= 3) & (df_tidy["fechas"].dt.month <= 6) & (df_tidy["fechas"].dt.year == 2020)]


df_grouped = df_tidy.groupby("fechas")["value"].sum().reset_index()
df_grouped["new_cases"] = df_grouped["value"].diff().fillna(df_grouped["value"])

plt.plot(df_grouped["fechas"], df_grouped["new_cases"])
plt.xlabel("Fecha")
plt.ylabel("Casos nuevos")
plt.title("Casos nuevos de COVID-19 por día")
plt.show()
#Se analiza un aumento progresivo de los casos a lo largo del tiempo, con un aumento significativo en la mitad del mes de mayo hasta la mitad de junio donde se disparan los casos


### Separar los casos por comuna y explorar la relación entre la densidad de población y la incidencia de COVID-19 en cada comuna
print(df_tidy)
print(df_tidy.shape)

cols= ['Comuna']
for col in cols:
  print(f'Columna {col}: {df_tidy[col].nunique()} subniveles')
  