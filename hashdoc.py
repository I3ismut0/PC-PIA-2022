import hashlib
import os


temp = []
with os.scandir('./') as ficheros:
    for fichero in ficheros:
        temp.append(fichero.name)
temp.remove(".git")

def valorhash():
    f = open ('hash.txt','w')
    for path in temp:
        file_obj= open (path,"rb")
        file= file_obj.read()
        Hash = hashlib.sha512(file)
        Hashed = Hash.hexdigest()
        f.write(path+":"+os.linesep+Hashed+ os.linesep)
    print("fin")
    f.close()

valorhash()
