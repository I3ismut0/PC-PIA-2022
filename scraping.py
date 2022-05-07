import re
import requests
from urllib.parse import urlsplit
# deque es un contenedor similar a una lista con anexos rápidos y ventanas emergentes en cada extremo
from collections import deque
from bs4 import BeautifulSoup
# pandas para formatear correos electrónicos en un DataFrame para una mayor manipulación
import pandas as pd

def scraping_url(original_url):
    # inicializamos un deque para guardar las URL no extraídas, un conjunto para las URL
    # extraídas y un conjunto para guardar los correos electrónicos extraídos con éxito del sitio web
    # https://dirind.com/dae/componentes_electronicos_general1.html
    unscraped = deque([original_url])

    #Los elementos en Setson únicos, no se permiten elementos duplicados
    scraped = set()

    emails = set()

    while len(unscraped):
        url = unscraped.popleft()
        scraped.add(url)

    # usamos urlsplit para extraer diferentes partes del archivo url
    # urlsplit devuelve una tupla de 5:
    # (esquema de direccionamiento, ubicación de red, ruta, consulta, identificador de fragmento)
        if not 'https' in url:
            print('No es una url')
        else:
            parts = urlsplit(url)

            base_url = "{0.scheme}://{0.netloc}".format(parts)
            if '/' in parts.path:
                path = url[:url.rfind('/')+1]
            else:
                path = url

            print("Descomprimiendo URL %s" % url)
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema,
                    requests.exceptions.ConnectionError):
                continue
        # Extraiga todas las direcciones de correo electrónico
        # de la respuesta mediante una expresión regular y agréguelas al emailconjunto
            new_emails = set(re.findall
                             (r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",
                              response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, 'lxml')

            for anchor in soup.find_all("a"):
                if "href" in anchor.attrs:
                    link = anchor.attrs["href"]
                else:
                    link = ''

                    if link.startswith('/'):
                        link = base_url + link

                    elif not link.startswith('http'):
                        link = path + link

                    if not link.endswith(".gz"):
                        if not link in unscraped and not link in scraped:
                            unscraped.append(link)

        df = pd.DataFrame(emails, columns=["Email"])
        df.to_csv('email.csv', index=False)
