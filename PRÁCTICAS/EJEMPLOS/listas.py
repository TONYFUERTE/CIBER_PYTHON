from inspect import currentframe as nu
from inspect import getframeinfo as get

#Listas
lista = [1,2,3,4,5]; print(lista)
lista.append(3); print(lista)
lista_nueva = lista.append(8); print(lista_nueva) #No podemos asignar a una variable a un comando, nos da None.
lista_nueva = lista; lista_nueva.append(8); print(lista_nueva)
print(lista_nueva.count(3)) #Número de veces que se repite un elemento
print(lista_nueva.index(4)) #Índice de la primera aparición de un elemento
lista_nueva.remove(3); print(lista_nueva) #Borra el primer elemento que coincida con el dado

mi_lista = ['a','b','c']; print(type(mi_lista))
mi_lista2 = ['d','e','f']
print(get(nu()).lineno,end=": ");   print(mi_lista[0]) #posición 0
print(get(nu()).lineno,end=": ");   print((mi_lista[0:2])) #de la 0 a la 1
print(get(nu()).lineno,end=": ");   print(mi_lista[::-1]) #Invierte
print(get(nu()).lineno,end=": ");   print(mi_lista + mi_lista2) # se pueden sumar listas
#ELIMINAR
print(get(nu()).lineno,end=": "); lista3 = mi_lista + mi_lista2; print(lista3)
print(get(nu()).lineno,end=": "); lista3.pop(); print(lista3)
print(get(nu()).lineno,end=": "); lista3.pop(0); print(lista3)
#ORDENAR
print(get(nu()).lineno,end=": "); lista3.append("r"); lista3.append("m"); lista3.append("a");print(lista3)
print(get(nu()).lineno,end=": "); lista3.sort(); print(lista3) 

