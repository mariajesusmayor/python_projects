from bs4 import BeautifulSoup
import requests
import os

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

res.status_code

len(res.text)

directory = "/home/mariajesus/ownCloud/Programacion/Python"

os.chdir(directory)

playFile = open("RomeoAndJuliet.txt", "wb")

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

