<<<<<<< HEAD
#! python3

from bs4 import BeautifulSoup
import requests

url = "http://www.aemet.es/es/portada"
response = requests.get(url)
try:
   response.raise_for_status()
except:
   print("Hay algún problema con la URL")
soup = BeautifulSoup(response.text, "html.parser")

selecMuni = soup.select(".texto_municipio_portada")
selecMaxim = soup.select(".texto_maxima_mun_portada")
selecMinim = soup.select(".texto_minima_mun_portada")

try:
   len(selecMuni)==len(selecMaxim) and len(selecMaxim)==len(selecMinim):
except:
   print("")

municipios = []
maximas = []
minimas = []

for i in (range(len(selecMuni))):
   muni = selecMuni[i].text.encode("utf-8").strip()
   municipios.append(muni)
   maxim = selecMaxim[i].text.encode("utf-8").strip()
   maximas.append(maxim)
   minim = selecMinim[i].text.encode("utf-8").strip()
   minimas.append(minim)

   print("La temperatura máxima prevista para mañana en " + str(municipios[i]) + " es de " + str(maximas[i]) + " y la mínima es de " + str(minimas[i]))





=======
#! python3

from bs4 import BeautifulSoup
import requests

url = "http://www.aemet.es/es/portada"
response = requests.get(url)
try:
   response.raise_for_status()
except:
   print("Hay algún problema con la URL")
soup = BeautifulSoup(response.text, "html.parser")

selecMuni = soup.select(".texto_municipio_portada")
selecMaxim = soup.select(".texto_maxima_mun_portada")
selecMinim = soup.select(".texto_minima_mun_portada")

try:
   len(selecMuni)==len(selecMaxim) and len(selecMaxim)==len(selecMinim):
except:
   print("")

municipios = []
maximas = []
minimas = []

for i in (range(len(selecMuni))):
   muni = selecMuni[i].text.encode("utf-8").strip()
   municipios.append(muni)
   maxim = selecMaxim[i].text.encode("utf-8").strip()
   maximas.append(maxim)
   minim = selecMinim[i].text.encode("utf-8").strip()
   minimas.append(minim)

   print("La temperatura máxima prevista para mañana en " + str(municipios[i]) + " es de " + str(maximas[i]) + " y la mínima es de " + str(minimas[i]))





>>>>>>> a3c79e1e64543b0d6f078d5527564506ecdfc6db
