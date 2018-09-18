import bs4, requests

#res = requests.get("https://www.macnificos.com/zagg-rugged-messenger-funda-ipad-97-2017-2018#sku-ZAG0031")

res = requests.get("https://nostarch.com/impracticalpythonprojects")

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

caracteristicas = []

seleccionArticulo = soup.select("h1.page-header")

articulo = seleccionArticulo[0].text.strip()

seleccionPrecio = soup.select("div.form-item.form-item-attributes-1.form-type-radio.radio")

precio = seleccionPrecio[0].text.strip()

seleccionDatos = soup.select("div.field.field-name-field-isbn13.field-type-text.field-label-inline.clearfix.clearfix")

datos = seleccionDatos[0].text.strip()

caracteristicas.append(articulo)
caracteristicas.append(precio)
caracteristicas.append(datos)

print(caracteristicas)





