#OPERADORES DE COMPARACIÓN
mi_variable = 'hola mundo'
mi_bool = 10==25
print(f"10==25 es {mi_bool}")
mi_bool = 5+5 == 18-8 #Acepta operaciones
print(f"5+5 == 18-8 es {mi_bool}")

#comparadores strings
mi_bool = 'blanco'=='negro'
print(f"'blanco' == 'negro' es {mi_bool}")
mi_bool = 'blanco'=='Blanco' #es case-sensitive; 
print(f"'blanco'=='Blanco' es {mi_bool}")
mi_bool = 'blanco'=='Blanco'.lower()
print(f"'blanco'=='Blanco'.lower() es {mi_bool}")

print(f'100.0==100: {100.0==100}') #Aunque sea distinto tipo el valor es el mismo será True
print(f'100.0 != 100: {100.0!=100}') #Aunque sea distinto tipo el valor es el mismo será True

