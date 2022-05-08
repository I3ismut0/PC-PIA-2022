from hashlib import md5
from virus_total_apis import PublicApi

API_KEY = "0b0ee841de83cfe9a05232f3a7d820e724babb33283ac182567cf988fad4bd99"
api = PublicApi(API_KEY)
def total(args):
    API_KEY = "0b0ee841de83cfe9a05232f3a7d820e724babb33283ac182567cf988fad4bd99"
    api = PublicApi(API_KEY)
    with open(args, "rb") as f:
        file_hash = md5(f.read()).hexdigest()
    response = api.get_file_report(file_hash)
    response1= api.scan_file(args)

    if response["response_code"] == 200:
        if response["results"]["positives"] > 0:
            print("Archivo malicioso.")
        else:
            print("Archivo seguro.")
    else:
        print("No ha podido obtenerse el análisis del archivo.")

def escanear(args):
    response = api.scan_file(args)

# Obtener análisis de un dominio.
def escaneardominio(args):
    response = api.get_url_report(args)

# Obtener análisis de una dirección de IPv4.
def escanearip(args):
    response = api.get_ip_report(args)

# Comentar en un archivo identificado por MD5.
def comentarchivo(args):
    with open(args, "rb") as f:
        api.put_comments(md5(f.read()).hexdigest(), "Excelente herramienta.")

# Comentar en una URL.

def comenturl(args,comentario):
    api.put_comments(args, comentario)
