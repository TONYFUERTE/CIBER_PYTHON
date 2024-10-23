# def saludar():
#     print('Hola')

# saludar()

# def saludar_persona(nombre):
#     print('Hola ' + nombre)

# saludar_persona('Pepe')

# def multiplicar(num1,num2):
#     return num1 * num2

# resultado = multiplicar(5,10)
# print(resultado)

# def dividir(num1,num2):
#     total= num1 / num2
#     return total

# resultado= dividir(200,5)
# print(resultado)

# # FUNCIONES DINÁMICAS

# def chequear_3_cifras(numero):
#     return numero in range(100,1000)
# valor = int(input('Introduzca Valor de tres cifras: '))
# resultado = chequear_3_cifras(valor)
# print(resultado)


# def chequear_v2(lista):
    
#     lista_3_cifras = []
#     for n in lista: 
#         if n in range(100,1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
#     return lista_3_cifras
# resultado2 = chequear_v2([555,99,600])
# print(resultado2)

#Una de las prácticas

# def todos_positivos (lista):
#     i = 0
#     for plus in lista:
#         if plus > 0:
#             lista_numeros.append(plus)
#             i+=1
#         else:
#             pass
#     if i == len(lista) :
#         return True
#     else:
#         return False

# lista_numeros = []
# resultado = todos_positivos([45,56,-9])
# print(resultado,lista_numeros)

#EJEMPLO DE FUNCIÓN

precios_cafe = [('capuchino', 1.5),('Expresso',1.2),('Moka',1.9)]

#Un for simple para recorrer la lista de tuplas e imprimir todos los elementos. 
# for bebidas,precio in precios_cafe:
#     print(f"Bebida {bebidas}, precio: {precio} €")
#     print(f"Precio + IGIC: {precio * 1.07}")
    
#Una función para saber el producto más caro

# def coffe_more_expensive (lista_precios):
#     precio_mayor = 0
#     cafe_mas_caro = ''
#     for cafe,precio in lista_precios:
#         if precio > precio_mayor:
#             precio_mayor = precio
#             cafe_mas_caro = cafe
#         else:
#             pass
    
#     return cafe_mas_caro, precio_mayor

# print(f"El café más caro es {coffe_more_expensive(precios_cafe)[0]} a {coffe_more_expensive(precios_cafe)[1]} €")
# cafe,precio = coffe_more_expensive(precios_cafe)

# print(cafe,precio)

#INTERACCIÓN ENTRE FUNCIONES

#Juego de los palitos. Pierde el que coja el palito más corto
# from random import shuffle #Importamos shuffle para dar un orden aleatorio a la lista
# palitos = ['-', '--', '---', '----']

# #mezclar palitos
# def mezclar(lista):
#     shuffle(lista)
#     return lista

# # Pedir intento al usuario
# def probar_suerte():
#     intento = 0
#     while intento not in [1,2,3,4]:
#         intento = int(input("Elige un número del 1 al 4: "))

#     return intento

# #Verificar palito
# def chequear_intento(lista,seleccion):
#     if lista[seleccion-1] == '-':
#         print(f'Has perdido, te ha tocado el palito más pequeño: palito = {lista[seleccion-1]}')
#     else:
#         print(f'Has tenido suerte, tu palito no es el más pequeño. Palito = {lista[seleccion-1]}')
        
# palitos_mezclados = mezclar(palitos);
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados,seleccion)

#ARGUMENTOS INDEFINIDOS(*arg)

#Añadiendo el asterisco no tiene que 
# estar definido el número de argumentos, 
# es dinámico.
# def suma(*argumentos):
#     return sum(argumentos) #retorna la suma

# print(suma(5,7,9,12,3,5))

#ARGUMENTOS INDEFINIDOS (**kwarg)
#se le puede pasar un nombre y un valor

# def suma(**kwargs):
#     print(type(kwargs)) #Nos devuelve un diccionario
#     total = 0
#     for clave,valor in kwargs.items():
#         print(f"{clave} = {valor}")
#         total += valor
#     return total
# print(f'La suma de todos los valores es {suma(x=3, y=5, z=2)}')

#Mexcla de argumentos directos, *args, *kwargs

def mexcla(num1,num2,*args,**kwargs):
    
    print(f'El valor num1 es: {num1}')
    print(f'El valor nu21 es: {num2}')

    for arg in args:
        print(f"arg = {arg}")
    for clave,valor in kwargs.items():
        print (f"{clave} = {valor}")

mexcla(15,21,44,56,72,84, x=6, m=8)

argumentos = [44,56,72,84]
keyargs = {'x':6, 'm':8}

mexcla(15,21,*argumentos, **keyargs)
