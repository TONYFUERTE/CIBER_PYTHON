if (10 > 9):
    print('Entra en 10 > 9')
    
x = True
if x:
    print('Entra en el if con x')
if 5==2:
    print('Entra en 5==2')
elif 5!=2:  
    print('Entra en 5!=2')
    
mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No sé que animal tienes. ')
    
#ANIDAR IF
edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad.')
    if calificacion >= 7:
        print('Aprobado.')
    else:
        print('No Aprobado')
else:
    print('Eres adulto')
    
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
if (num1 > num2):
    print(f"{num1} es mayor que {num2}")
elif (num1 < num2):
    print(f"{num2} es mayor que {num1}")
elif (num1 == num2):
    print(f"{num1} es igual que {num2}")
    