#SÓLO LECTURA 'r'

# archivo = open('prueba.txt','r') #Este es el modo que viene por defecto. SÓLO LECTURA

# archivo.write('soy el nuevo texto') #Da un error porque hemos definido abrirlo como sólo lectura

#CREAR Y SOBREESCRIBIR 'w'

archivo = open('prueba1.txt', 'w')  #Crea un nuevo archivo

archivo.write('Soy el nuevo archivo')
archivo.write('Soy el nuevo archivo sobreescrito') #No añade sato de línea. Podemos añadirlo con \n o con triple comilla """ """

#Si volvemos a aplicar un write en otra ejecución sobreescribe. 

#CREAR Y ESCRIBIR AL FINAL 'a'

archivo2 = open('prueba2.txt', 'a')

archivo2.write('bienvenido')














archivo.close()

