lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) + 1 #Para obtener el índice de cada letra + 1
    print(f"Letra {numero_letra}: {letra}")
    
lista = ['Pablo','Luis','Julia','Juan','Eugenio']
for nombre in lista:
    if nombre.lower().startswith('l'):
        print(nombre)
    else:
        print("Nombre que no empieza con l")

numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(f"mi_valor valdrá al finalizar el loop es {mi_valor}")

palabra = 'python'
for letra in palabra:
    print(letra, end=' ')
print()
for letra in 'palabra': #podemos incluir directamente el string
    print(letra, end=' ')
print()

#ITERAR LISTAS
for a in [1,2,3,7,9,6]:
    print(a, end=' ')
print()
for a in [1,2,[3,7],9,6]: #Podemos incluir listas dentro de listas pero lo considera un sólo elemento
    print(a)
print()
for a,b in [[1,2],[3,7],[9,6]]: #Si itera con tantas variables como tenga cada lista la asocia a cada variable
    print(a)
    print(b)
print()

#ITERAR DICCIONARIOS
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic:
    print(item, end=' ') #Se imprimen sólo las claves.
print()
    
for item in dic.items():
    print(item, end=' ') #Se imprimen todo el item.
print()

for a,b in dic.items():
    print(f"Para la key {a}, el value es {b}.", end=' ') #podemos separar clave y valor en variables
print()

for item in dic.values():
    print(item, end=' ') #Se imprimen los valores

