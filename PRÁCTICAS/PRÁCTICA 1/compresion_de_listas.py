<<<<<<< HEAD
lista = [letra for letra in 'python']
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n/2 for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)

lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]
print(lista)
=======
# lista = [letra for letra in 'python']
# print(lista)

# lista = [n for n in range(0,21,2)]
# print(lista)

# lista = [n//2 for n in range(0,21,2)]
# print(lista)

# lista = [n for n in range(0,21,2) if n * 2 > 10]
# print(lista)

# lista = [n if n * 2 > 10 else 'no CUMPLE' for n in range(0,21,2) ]
# print(lista)
>>>>>>> ec56d65e261b41a4f790831640bc28439029a595

cms = [10,20,30,40,50]
mts = [cm *0.01 for cm in cms]
print(mts)