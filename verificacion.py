import re
import smtplib
import dns.resolver

def email_verf(inputAddress):
    # Dirección utilizada para el comando SMTP MAIL FROM
    fromAddress = 'corn@bt.com'

    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

    #inputAddress = input('Inserte el correo a verificar :')
    addressToVerify = str(inputAddress)

    match = re.match(regex, addressToVerify)
    try:
        if match == None:
    	    print('El correo no coincide')
    	    raise ValueError('Error Syntax')
    except:
        print('El correo no se encuentra en el archivo')

    # Obtener dominio para búsqueda de DNS

    if not '@' in inputAddress:
        print('Por lo tanto no es un correo')
    else:
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
