__author__ = 'PabloSFK'

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos
eq = soup.find_all('span', class_='nombre-equipo')

#Puntos
pt = soup.find_all('td', class_='destacado')

equipos = list()

for i,j in enumerate(eq):
    if i > 19:
        break
    equipos.append(j.text)

print(equipos)


puntos = list()

for i,j in enumerate(pt):
    if i > 19:
        break
    puntos.append(j.text)

print(puntos)

df = pd.DataFrame({'Nombre': equipos, 'Puntos': puntos}, index=list(range(1, 21)))
df.to_csv('Clasificacion.csv')
print(df)
