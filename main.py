#Recuerda importar las librerias
import argparse
import logging
import sphinx
import sys
import subprocess
from hashdoc import valorhash
from scraping import scraping_url
from verificacion import email_verf
from socketscript import socketd
from verip import ipleef
from virustotal import total
def main():
    parser = argparse.ArgumentParser(
        description="suite de seguridad",
        epilog="HASH:  ,WEBSCRAPING: Para esta opcion se necesita la url de una pagina web, VERIFICACION DE CORREO: se necesita un correo que este dentro del archivo generado por el webscraping, VER PUERTOS ABIERTOS: se necesita una direccione ip la cual puedes buscar con el comando para ver ip's disponibles")
    parser.add_argument('-hash','-vh',
                        help='Obtiene el valor hash de todos los archivos contenidos en esta carpeta.')
    parser.add_argument('-webscraping', "-s",
                        help = "Obtener correos de una pagina web")
    parser.add_argument('-verificacion',"-v",
                        help= "Verifica un correo del archivo previamente generado")
    parser.add_argument('-verip',"-ip", action='store_true', default=False,
                        help='Ver direcciones ip disponibles')
    parser.add_argument('-socket',"-so",
                        help='Ver puertos abiertos y cerrados de una direccion ip')
    parser.add_argument('-virus',"-vi",
                        help='Checar si un archivo es malicioso')
    if __name__ =="__main__":
        args = parser.parse_args()

        if args.hash:
            valorhash()
        elif args.webscraping:
            scraping_url(args.webscraping)
        elif args.verificacion:
            email_verf(args.verificacion)
        elif args.verip:
            ipleef()
        elif args.socket:
            socketd(args.socket)
        elif args.virus:
            total(args.virus)
main()
