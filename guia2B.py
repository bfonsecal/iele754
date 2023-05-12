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


plt.show(df_tidy)
