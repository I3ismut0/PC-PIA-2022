#Recuerda importar las librerias
import argparse
import logging
import sphinx
import subprocess
from hashdoc import valorhash
from scraping import scraping_url
from verificacion import email_verf
def main():
    parser = argparse.ArgumentParser(
        description="suite de seguridad",
        epilog="HASH:  ,WEBSCRAPING: Para esta opcion se necesita la url de una pagina web, VERIFICACION DE CORREO: se necesita un correo que este dentro del archivo generado por el webscraping")
    parser.add_argument('-hash','-vh',
                        help='Obtiene el valor hash de todos los archivos contenidos en esta carpeta.')
    parser.add_argument('-webscraping', "-s",
                        help = "Obtener correos de una pagina web")
    parser.add_argument('-verificacion',"-v",
                        help= "Verifica un correo del archivo previamente generado\n -Se necesita un correo del archivo generado")

    if __name__ =="__main__":
        args = parser.parse_args()

        if args.hash:
            valorhash()
        elif args.webscraping:
            scraping_url(args.webscraping)
        elif args.verificacion:
            email_verf(args.verificacion)
main()
