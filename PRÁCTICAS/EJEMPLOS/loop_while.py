monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas.")
    monedas -= 1
else: print('No tengo más monedas.')

respuesta = 's'
while respuesta == 's':   #Número de iteraciones controladas por el usuario
    respuesta = input("quieres seguir? (s/n): ")
else: 
    print('Gracias')

#PASS, para poder seguir escribiendo código sin necesidad de implementar código en el while
while respuesta == 's':
    pass

#BREAK, para interrumpir el bucle
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#CONTINUE, para saltarse la iteración y seguir iterando
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)

