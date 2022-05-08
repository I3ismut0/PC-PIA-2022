#socket
import socket
import sys
import subprocess

def socketd(ip):
    print("IP",ip,type(ip))
    try:
        for port in range (80,200):
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print("puerto {}:\t Abierto".format(port))
            else:
                print("puerto {}:\t Cerrado".format(port))
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Error de conexion")
        sys.exit()
