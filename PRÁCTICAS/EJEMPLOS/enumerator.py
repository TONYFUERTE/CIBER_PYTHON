lista = ['a','b','c']

for index,item in enumerate(lista):
    print(index,item)
    
for index,item in enumerate(range(50,55)):
    print(index,item)

mi_tuple = list(enumerate(lista)) #lista de tuplas con el índice y el valor
print(mi_tuple)