import hashlib
import os


temp = []

with os.scandir('./') as ficheros:
    for fichero in ficheros:
        temp.append(fichero.name)
temp.remove(".git")
temp.remove("__pycache__")

def valorhash(pathuno):
    if len(pathuno) < len(temp):
        f = open ('hash.txt','w')
        for path in temp:
            file_obj= open (path,"rb")
            file= file_obj.read()
            Hash = hashlib.sha512(file)
            Hashed = Hash.hexdigest()
            f.write(path+":"+os.linesep+Hashed+ os.linesep)
        print("fin")
        f.close()
    else:
        print(pathuno)
        f = open ('hashselected.txt','w') 
        file_obj= open (pathuno,"rb")
        file= file_obj.read()
        Hash = hashlib.sha512(file)
        Hashed = Hash.hexdigest()
        f.write(pathuno+":"+os.linesep+Hashed+ os.linesep)
        print("fin")
        f.close()
        
#pathuno = input("incerte ruta de un archivo en especifico\n")
#valorhash(pathuno)
