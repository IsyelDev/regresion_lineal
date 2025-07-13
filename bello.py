from bs4 import BeautifulSoup
import requests

url = "https://naruto-official.com/es"
resultado = requests.get(url)
sopa = BeautifulSoup(resultado.text, "lxml")

datos = []

for a in sopa.select(".css-d26lzs"):
    img = a.select_one("img")
    if img:
        datos.append(img["src"])

# Descargar la primera imagen
img_url = "https://naruto-official.com/es" + datos[0]
img_data = requests.get(img_url).content

with open("mi_imagen.jpg", "wb") as f:
    f.write(img_data)
