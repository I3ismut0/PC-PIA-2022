#Recuerda importar las librerias
import argparse
import logging
import sphinx
import subprocess
from hashdoc import valorhash

def main():
    parser = argparse.ArgumentParser(
        description="suite de seguridad",
        epilog="Mucho textoxd")
    parser.add_argument('-vh',
                        help='Obtiene el valor hash de todos los archivos contenidos en esta carpeta.')

    args = parser.parse_args()
    parser.print_help()
    

if __name__ =="__main__":
    main()