import re
import smtplib
import dns.resolver

# Dirección utilizada para el comando SMTP MAIL FROM
fromAddress = 'corn@bt.com'

regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

with open("email.csv") as archivo:
    print(archivo.read())

inputAddress = input('Inserte el correo a verificar :')
addressToVerify = str(inputAddress)

match = re.match(regex, addressToVerify)
if match == None:
	print('Error Syntax')
	raise ValueError('Error Syntax')

# Obtener dominio para búsqueda de DNS
splitAddress = addressToVerify.split('@')
domain = str(splitAddress[1])
print('Dominio:', domain)

# Búsqueda de registros MX
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)


# Configuración de SMTP lib (use el nivel de depuración para una salida completa)
server = smtplib.SMTP()
server.set_debuglevel(0)

# Conversación SMTP
server.connect(mxRecord)
server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
server.mail(fromAddress)
code, message = server.rcpt(str(addressToVerify))
server.quit()

# Asumir que la respuesta SMTP 250 es exitosa
if code == 250:
	print('Existe')
else:
	print('No existe')
