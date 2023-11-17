eli=open("eli.txt","w") 
eli.write("linea creada.\n") 
eli.write("nueva linea.\n") 
eli.write("linea creada 2.\n")  
eli.close()

eli=open('eli.txt','r')
contenido= eli.read()
print (contenido)
eli.close()

eli=open("eli.txt","r")
linea=eli.readline()
while linea!='':
    print(linea, end='')
    linea=eli.readline()
eli.close()


eli=open("eli.txt","r")
for linea in eli:
    print(linea, end='')
eli.close()


eli=open("eli.txt","r")
lineas=eli.readlines()
print('El archivo tiene', len(lineas), 'líneas')
print('El contenido del archivo')
for linea in lineas:
    print(linea, end='')
eli.close()


eli=open("eli.txt","a")
eli.write("ok \n")
eli.write("ño\n")
eli.close()
eli=open("eli.txt","r")
contenido=eli.read()
print(contenido)
eli.close()

eli=open("eli.txt","r+") 
contenido=eli.read()
print(contenido)
eli.write("braulio\n")
eli.write("otro eric\n")
eli.close()


eli=open("eli.txt","w", encoding="utf-8") 
eli.write("enserio.\n") 
eli.write("neta.\n") 
eli.write("bueno.\n")  
eli.close() 