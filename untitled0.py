import os
import requests
from bs4 import BeautifulSoup
requete = requests.get("https://www.jetbrains.com/pycharm/")
page = requete.content
soup = BeautifulSoup(page,features="lxml")
p = soup.find_all("p", {"class": "story__user-name"})
liste_nom = [elt.string.strip() for elt in p]

print(liste_nom)
