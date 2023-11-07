import requests
from bs4 import BeautifulSoup
import json

import requests
from bs4 import BeautifulSoup
import json

def scrape_aliexpress(search_term):   
    url = requests.get(f'https://es.aliexpress.com/w/wholesale-{search_term}.html?spm=a2g0o.productlist.search.0')
    soup = BeautifulSoup(url.content, 'html.parser')
    productos = soup.find_all("div", class_="multi--outWrapper--SeJ8lrF card--out-wrapper") 
    print(productos)
    product_data = []
    for prod in productos:
        # Extraer el nombre del producto
        name = prod.find("h1", class_="multi--titleText--nXeOvyr").text.strip()
        # Extraer la imagen del producto
        img_tag = prod.find("img", class_="multi--img--1IH3lZb product-img")
        if img_tag is not None:
            image = "https:" + img_tag['src']
        else:
           print("No se encontró la imagen del producto")
            
        # Extraer el precio del producto
        price_text = prod.find("div", class_="multi--price--1okBCly").text.strip()
        price_text = price_text.replace('COP', '').replace(',', '')  # Eliminar 'COP' y las comas
        price = float(price_text)  # Convertir el precio a un número
        # Extraer el enlace del producto
        link= prod.find("a", class_="multi--container--1UZxxHY cards--card--3PJxwBm search-card-item").get('href')
        if link.startswith("//"):
            link = "https:" + link

        # Añadir el producto a la lista de productos
        product_data.append({
            'Product': name,
            'Price': price,
            'Link': link,
            'Image': image
        })

    # Convertir la lista de productos en un objeto JSON y devolverlo
    return json.dumps(product_data, indent=4)

print(scrape_aliexpress('iphone'))

    # Convertir la lista de productos en un objeto JSON y devolverlo
    return product_data
