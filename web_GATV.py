from bs4 import BeautifulSoup
import requests
import os, os.path, csv

url = "http://www.gatv.ssr.upm.es/index.php/publicaciones/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

publicaciones = soup.find_all(class_ = 'toggle_content invers-color')

print(publicaciones)

print("objeto find all " + str(type(publicaciones)))

publicaciones_cadena = str(publicaciones)

#print(publicaciones_cadena)

rotulos = soup.select("h4")
print("esto es el tipo de un rótulo " + str(type(rotulos)))



print(rotulos)

print("este es el rótulo número 1" + str(rotulos[0]))

print(len(publicaciones))

print(publicaciones[14])

print(type(publicaciones[14]))

noticias = soup.find_all(class_ = "news_link")

print(noticias)
