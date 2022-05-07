import hashlib
import os

temp = open("datos.txt",'r').read().split('\n')

def valorhash():
    f = open ('hash.txt','w')
    for path in temp:
        file_obj= open (path,"rb")
        file= file_obj.read()
        Hash = hashlib.sha512(file)
        #print(Hash)
        Hashed = Hash.hexdigest()
        #print(Hashed)
        f.write(path+":"+os.linesep+Hashed+ os.linesep)
    print("fin")
    f.close()

#print(temp)
valorhash()
