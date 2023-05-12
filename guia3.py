import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats 


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

from scipy.stats import norm
import matplotlib.pyplot as plt

# Ajuste de distribución normal a los datos
mu, std = norm.fit(df_grouped["new_cases"])

# Graficar histograma de datos y curva ajustada
plt.hist(df_grouped["new_cases"], bins=100, density=True, alpha=0.6, color='g')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
plt.xlabel("Casos nuevos")
plt.ylabel("Densidad")
plt.title("Ajuste de distribución normal")
plt.show()

#HISTOGRAMA
#plt.hist(df_grouped['value'],bins=100,density=True)

#plt.xlabel('Value')
#plt.ylabel('Density')

#params_fit = scipy.stats.powerlaw.fit(df_grouped['value'])
#x = np.linspace(np.min(df_grouped['value']), np.max(df_grouped['value']), 100)

# Graficar la curva de ajuste
#plt.plot(x, scipy.stats.powerlaw.pdf(x, *params_fit), label='Power-law Distribution')
#plt.legend()  # Mostrar leyenda

#plt.show()
