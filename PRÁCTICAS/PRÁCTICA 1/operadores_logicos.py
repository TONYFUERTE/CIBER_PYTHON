mi_bool = 4 < 5 < 6
mi_bool2 = 4 < 5 > 6
print(f"4 < 5 < 6 es {mi_bool}")
print(f"4 < 5 > 6 es {mi_bool2} ")

#Se puede hacer con el operador "and" y "or"
mi_bool = 4 < 5 and 5==2+3
mi_bool = (4 < 5) and ('perro'== 'PERRO')
print(f"(4 < 5) and ('perro'== 'PERRO' es {mi_bool}")
mi_bool = (4 < 5) or (5==2+4) #Con paréntesis es más visual y mejor código
print(f"4 < 5 and 5==2+3 es {mi_bool}")
mi_bool = (4 < 5) or (5==2+4)
print(f"(4 < 5) or (5==2+4) es {mi_bool}")

texto = "Esta frase es breve"
mi_bool = ('frase' in texto) and ('es' in texto)
print(f"('frase' in texto) and ('es' in texto) es {mi_bool}")

#NEGACIÓN
mi_bool = not 'a' == 'a'
print(f"not 'a' == 'a' es {mi_bool}")
mi_bool = not('a' == 'A') #Con paréntesis es más visual 
print(f"not('a' == 'A') es {mi_bool}")
mi_bool = not('a' != 'A') #Con paréntesis es más visual 
print(f"not('a' != 'A') es {mi_bool}") #Doble negación







