archivo="colores.txt"
f = open(archivo,"a+")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()