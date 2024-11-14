import os

ruta = os.getcwd() #Nos da la ruta actual
print(ruta)

ruta_distinta = os.chdir('C:\\CLASE\\PUK') #Obtener nueva ruta
archivo = open('Texto_de_archivo_en_otra_ruta.txt')
print(archivo.read())

# nuevo_directorio = os.makedirs('C:\\CLASE\\PUK\\PYTHON\\Repositorio\\PRÁCTICAS\\EJEMPLOS\\Carpeta_nueva') #Crea Carpeta_nueva

ruta2 = 'C:\\CLASE\\PUK\\Texto_de_archivo_en_otra_ruta.txt'

obtener_archivo = os.path.basename(ruta2) #Obtiene el archivo si está especificado en la ruta
print(obtener_archivo)
archivo = open(obtener_archivo)
print(archivo.read())

obtener_ruta = os.path.dirname(ruta2) #Obtiene hasta el último directorio
print(obtener_ruta)

# os.rmdir('C:\\CLASE\\PUK\\PYTHON\\Repositorio\\PRÁCTICAS\\EJEMPLOS\\Carpeta_nueva')  #Eliminar carpeta

#Como lo haríamos de sin aplicar métodos

archivo = open(ruta2) #Pero esta ruta está escrita en formato WINDOWS
print(archivo.read())

#Vamos a ver como podemos escribir una ruta para cualquier sistema operativo. 

from pathlib import Path   #Añadimos el método Path de pathlib

carpeta = Path('C:/CLASE/PUK')    #Estas rutas ya son operativas con cualquier sistema operativo
archivo = carpeta / 'Texto_de_archivo_en_otra_ruta.txt'   #Añadimos el archivo que queremos leer
mi_archivo = open(archivo)
print(mi_archivo.read())

#Nos podemos ahorrar una línea de código añadiendo el archivo a carpeta con esta 
carpeta = Path('C:/CLASE/PUK') / 'Texto_de_archivo_en_otra_ruta.txt' 
mi_archivo = open(carpeta)
print(mi_archivo.read())

