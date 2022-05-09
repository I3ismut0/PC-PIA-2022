# PC-PIA-2022

------------


## suite de seguridad
- Web scraping
- Escaneo de puertos
- Obtención de claves HASH
- Revisión de correos

## Requisitos 
Python 3.10.4 
Powershell 5.1.0
## Instalación
### Clonar el repositorio

	git clone https://github.com/I3ismut0/PC-PIA-2022
### Requirements.txt 
	Pip install -r requirements.txt 
## Funcionamiento

`[-h] [--hash HASH] [--webscraping WEBSCRAPING] [--verificacion VERIFICACION] [--verip] [--socket SOCKET]`

#####   --webscraping WEBSCRAPING, -s WEBSCRAPING
Obtener correos de una página web
###### Ejemplo
	python .\main.py  --webscraping “URL”
	python .\main.py  -s “URL”
##### --verificacion VERIFICACION, -v VERIFICACION
 Verifica un correo del archivo previamente generado
###### Ejemplo
	python .\main.py -v “correro electrónico”
	pyhton .\Main.py --verificacion  “correro electrónico”
##### --verip, -ip           Ver direcciones ip disponibles
###### Ejemplo
	pyhton .\Main.py --verip “IP”
	pyhton .\Main.py -ip  “IP”
##### --socket SOCKET, -so SOCKET
Ver puertos abiertos y cerrados de una dirección ip
###### Ejemplo
	python .\main.py  --socket “IP”
	python .\main.py  -so “IP”
##### --virus VIRUS, -vi VIRUS
Checar si un archivo es malicioso
###### Ejemplo
	python .\main.py  --virus “PATH”
	python .\main.py  -vi “PATH”

## Observaciones
> 
#### HASH:
Genera un Archivo .txt con la clave hash junto al nombre del archivo analizado
#### WEBSCRAPING:
Para esta opción se necesita la URL de una página web
#### VERIFICACION DE CORREO:
se necesita un correo que este dentro del archivo generado por el webscraping.
#### VER PUERTOS ABIERTOS:
Se necesita una direccione IP la cual puedes buscar con el comando para ver IP's disponibles.[80;200]
> 
------------
**Gracias a todos los que hicieron esto posible.**
