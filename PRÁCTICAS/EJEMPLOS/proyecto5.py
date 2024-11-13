from random import choice


palabra = """El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida.
"""

lista_palabras = palabra.split()
# print(lista_palabras)
elegidas = []
for palabra in lista_palabras:
    if len(palabra)>5:
        elegidas.append(palabra)
elegida = choice(elegidas)
print(elegida)

def mostrar_guiones(elegida):
    numero_caracteres = len(elegida)
    ind = 0
    lista = []
    while numero_caracteres > ind:
        ind+=1
        lista.append('_')
    print (lista[::])
    return lista

lista = mostrar_guiones(elegida)

def elegir_letra (letra):
    if letra in elegida:
        indice = elegida.find(letra)
        print(indice)
        lista[indice]= letra
elegir_letra(input('Elija una letra: '))
print(lista)