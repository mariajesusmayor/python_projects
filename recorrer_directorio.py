import os, sys

directorioBase = "C:\\Users\\mjm\\ownCloud\\UOC\\2018-19_Sem01\\"

for raiz, carpeta, archivos in os.walk(directorioBase):
	print("esto es la raiz " + str(raiz))
	print("esto es la carpeta " + str(carpeta))
	print("esto es el archivo " + str(archivos))

print ("Hecho")