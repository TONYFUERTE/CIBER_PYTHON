menor = min(58,76,48,35)
mayor = max(58,76,48,35)
print(menor,mayor)

lista = 58,76,48,35
print(min(lista)) #se puede hacer con cualquier coleción: tuplas, diccionarios

nombre = ['Carlos','Patricia','Juan','Alicia', 'alicia']
print(min(nombre)) #Busca la primera en orden alfabético pero busca primero en las mayúsculas (ASCII)

dic = {'c1': 45, 'c2':11}
print(min(dic)) #Nos da la clave más pequeña
print(min(dic.values())) #Nos daría el valor más pequeño