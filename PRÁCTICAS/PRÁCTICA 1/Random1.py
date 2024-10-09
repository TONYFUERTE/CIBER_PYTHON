from random import *

aleatorio = randint(1,50)
print(aleatorio) #Valor entero  dentro del rango

aleatorio = uniform(1,50)
print(aleatorio) #Valor decimal con muchos decimales
print(round(aleatorio,1)) #Podemos usar el round para que nos de los decimales que queramos

print(random()) #Valor entre 0 y 1

colores = ['azul','rojo', 'verde', 'azul']
print(choice(colores)) #Devuelve un valor aleatorio de cualquier colección

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros) #Nos cambia la lista de forma aleatoria
print(numeros)