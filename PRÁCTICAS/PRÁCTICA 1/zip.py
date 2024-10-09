nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42, 62]

combinado = zip(nombres, edades)
print(combinado)  #Nos da el elemento zip pero es necesario pasarlos a lista para poder verlo

print(list(combinado))

#Se pueden combinar todas las listas que quieras
ciudades = ['Lima', 'Madrid', 'Méjico']
combinado = list(zip(nombres, edades, ciudades))
print(combinado)

#Podemos usarlos en un bucle
for nombre, edad, ciudad in combinado:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")