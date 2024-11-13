mi_tuple = (1,2,3,4)
print(mi_tuple)
print(type(mi_tuple))

mi_tuple = 6,7,8,9  #también se pueden escribir así, pero no es común
print(mi_tuple)

print(mi_tuple[2])
print(mi_tuple[-3])

# mi_tuple[1] = 15  #No se puede modificar una tupla

mi_tuple = (1,2,(10,20), 3,4)  #tupla dentro de otra tupla
print(mi_tuple[2][0])

#Hacer casting

mi_tuple = list(mi_tuple) #Lo cambiamos a lista
print(mi_tuple)
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple) #Lo cambiamos a tupla de nuevo
print(mi_tuple)
print(type(mi_tuple))

#Asignación a variables a los valores de una tupla
t = (1,2,3)
print(t)
x,y,z = t #Tiene que ser el mismo número de variables que de valores 
print(x,y,z)

t = (1,2,3,1)
print('La longitud de  t es: ' + str(len(t)))
print('Número de veces que se repite el 1:', str(t.count(1))) #Número de veces que se encuentra el valor 1
print('La posición en la que se encuentra el 2 es:' , str(t.index(2))) #Primera posición en que coincida con el valor
