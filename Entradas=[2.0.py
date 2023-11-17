Entradas=[
['correo','nombre','telefono'],
['juan@gmail.com','Juan','8123232323'],
['maria@gmail.com','Maria','5545454545'],
['diana@homail.com','Diana','4490909090']
]
with open("agenda.csv","w+") as f:
    for e in Entradas:
        f.write(f"{e[0]}|{e[1]}|{e[2]}\n")
import os
# Se imprime el contenido de la lista, para cotejar.
print(">> Contenido de la lista.\n")
print(Entradas)
# Revisa si existe el CSV, en cuyo caso, si existe el BAK lo elimina
# y renombra el CSV como BAK
if os.path.exists("agenda.csv"):
    if (os.path.exists("agenda.bak")):
        os.remove("agenda.bak")
        os.rename("agenda.csv","agenda.bak")
# Se escribe el contenido de la lista, usando with y F-String
with open("agenda.csv","w+") as f:
    for e in Entradas:
        f.write(f"{e[0]}|{e[1]}|{e[2]}\n")
# Se revisa el contenido del archivo.
print("\n>> Contenido del archivo.\n")
with open("agenda.csv") as f:
    print(f.read())