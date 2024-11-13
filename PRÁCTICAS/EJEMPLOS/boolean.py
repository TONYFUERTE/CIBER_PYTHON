var1 = True
var2 = False

print(type(var1),end=''); print(var1)

numero = 5 > 2+3
print(type(numero), end=''); print(numero)

numero = 5 == 2+3
print(numero)
numero = bool(5<6) #Se puede generar un booleano con bool()
print(type(numero), end=''); print(numero)
numero = bool() #Por defecto nos da el valor False
print('por defecto bool() nos da un boolean ' + str(numero))

lista = [1,2,3,4]
control = 5 in lista
print(type(control), end='');  print(control)  #Falso porque 5 no está en la lista. 

redes = ['Youtube', 'Facebook', 'Twitter', 'Whatsapp']
print(sorted(redes))
redes = [3, 6, 1, 4]
print(sorted(redes))