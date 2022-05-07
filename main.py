#Recuerda importar las librerias
import argparse
import logging
import sphinx
import subprocess
from hashdoc import valorhash
#from scraping import 

def main():
    parser = argparse.ArgumentParser(
        description="suite de seguridad",
        epilog="Mucho textoxd")
    parser.add_argument('-vh',
                        help='Obtiene el valor hash de todos los archivos contenidos en esta carpeta.')
    parser.add_argument( "-s",
                        help = "")
    parser.add_argument("-v",
                        help= "Verifica los correos electronicos de una lista previoamente generada.")

    args = parser.parse_args()
    parser.print_help()    

if __name__ =="__main__":
    main()