#SET ELIMINA LOS REPETIDOS

#Usando set sólo se puede usar un argumento por lo que hay que meterlo en una lista o una tupla
mi_set = set([1,2,3,4,5,2]) 
print(type(mi_set))
print(mi_set)

#Se puede escribir también entre llaves
mi_set = {1,2,3,4,5,3}  #Aquí no es necesario meterlo en listas o tuplas
print(mi_set)

#print(mi_set[1]) #Imprimir una posicióon NO LO PERMITE
#mi_set[0] = 2 #Asignar un nuevo valor a una posición NO LO PERMITE
# mi_set = set((1,2,3,4,[3,4],5)) #Incluir listas o diccionarios no lo permite pq son mutables
mi_set= set((1,2,3,4,(1,3,5,5),1,1,1,1,1,1,2,2,2)) #puedes incluir tuplas pero no las modifica
print(mi_set)

print(len(mi_set))
print(2 in mi_set)
print((1,3,5,5) in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
print(s1.union(s2))
s1.add(4)
print(s1)
s1.add(2) #Si ya existe no lo añade

s1.remove(2)
print(s1)
# s1.remove(6) #Si no existe remove da error, por eso usar mejor discard
s1.discard(6)
s1.pop() #Elimina un elemento aleatorio
s1.clear() #Vacía el set
print(s1)