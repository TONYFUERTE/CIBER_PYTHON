from pathlib import Path, PureWindowsPath
import os

carpeta = Path('C:\CLASE\PUK\Texto_de_archivo_en_otra_ruta.txt') 
print(carpeta.read_text()) #Nos da el texto del archivo
print(carpeta.name)    #Nos da el nombre del archivo
print(carpeta.suffix)   #Nos da la extensión
print(carpeta.stem)    #Nos da el nombre sin la terminación

if not carpeta.exists():  #Para ver si el archivo exite, devuelve True o False
    print('Este archivo no existe.')
else:
    print('El archivo exite')

print(PureWindowsPath(carpeta)) #Nos pasa la ruta a formato windows

#Obtener directorio principal y crear rutas.
base = Path.home()
print(base)

#Crear instancias de Path

guia = Path(base, "Europa","España","Canarias","Fuerteventura.txt")
print(guia)
guia2 = guia.with_name('La_Palma.txt')
print(guia2)

print(guia.parent)
print(guia.parent.parent)

#Obtener todos los archivos de una ruta

ruta = Path('C:\CLASE\PUK\PYTHON\Repositorio\PRÁCTICAS\EJEMPLOS')

for txt in Path(ruta).glob('*.txt'):  #Obtengo todos los archivos txt que tenemos en la ruta
    print(txt)

#Puedo obtener todos los archivos que tengo en la ruta y en las subcarpetas 

ruta = Path('C:\CLASE\PUK\PYTHON\Repositorio\PRÁCTICAS')
for txt in Path(ruta).glob('**\*.txt'):  #Obtengo todos los archivos txt que tenemos en la ruta
    print(txt)
    
#Para obtener rutas relativas desde un punto

desde_PUK = ruta.relative_to(Path("C:\CLASE\PUK"))
print(desde_PUK)

