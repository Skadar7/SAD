from requests import get
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt


response = get('https://wiki.alioth.net/index.php/Oolite_planet_list/Galaxy_1')
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('dd')

planets = []
X = []
Y = []

for quote in quotes:
    res = re.search(r'^#.{5}\w*.{2}\d*,\d*.', quote.text)
    if res:
        tmp = res.group(0)[5:].split()
        planets.append(tmp[0])
        coor = re.split(r',', tmp[1])
        X.append(coor[0][1:])
        Y.append(coor[1][:-1])

fig, ax = plt.subplots()
ax.scatter(X, Y)

for i, name in enumerate(planets):
    ax.annotate(name, (X[i], Y[i]))
