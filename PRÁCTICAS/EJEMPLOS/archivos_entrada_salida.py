mi_archivo = open('prueba.txt') 

# print(mi_archivo) #muestra el formato del archivo, no el archivo

#READ

#print(mi_archivo.read()) #Ahora con el método read ya lo lee

#READLINE

# print(mi_archivo.readline()) #Solo imprime una línea a medida que se ejecuta va leyendo las siguientes líneas
# print(mi_archivo.readline().rstrip()) #Podemos quitar el salto de línea del archivo con rstrip()
# print(mi_archivo.readline().upper())  #Son string por lo que podemos utilizar los métodos de string, como upper()

#ITERAR EN EL ARCHIVO

# for l in mi_archivo:
#     print('Aquí dice: ' + l)

#READLINES: Crea una lista con todas las líneas. No se aconseja para archivos muy grandes. 

print(mi_archivo.readlines())

#No hemos modificado el archivo original. Sólo hemos trabajado con él. 

mi_archivo.close() #Se debe cerrar el archivo al final