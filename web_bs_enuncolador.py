<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests
import os, os.path, csv

url = "https://enuncolador.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

articulo = soup.find_all(class_ = 'entry-content')

esteArticulo = soup.find(id = "post-378")

print(articulo)

print(type(articulo))

print(esteArticulo)

=======
from bs4 import BeautifulSoup
import requests
import os, os.path, csv

url = "https://enuncolador.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

articulo = soup.find_all(class_ = 'entry-content')

esteArticulo = soup.find(id = "post-378")

print(articulo)

print(type(articulo))

print(esteArticulo)

>>>>>>> caa7a19daf82ef17cbd26673297aabeac62a1417
