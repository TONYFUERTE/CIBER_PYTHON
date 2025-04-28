# #ACTIVIDAD HERENCIA 1

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
        
# class Alumno(Persona):
#     pass

# #ACTIVIDAD HERENCIA 2

# class Mascota:
#     def __init__(self, nombre, edad, numero_patas):
#         self.nombre = nombre
#         self.edad = edad
#         self.numero_patas = numero_patas
        
# class Perro(Mascota):
#     pass

# #ACTIVIDAD HERENCIA 3

# class Vehiculo:
#     def acelerar(self):
#         print('Acelera')
#     def frenar(self):
#         print('Frena')

# class Automovil(Vehiculo):
#     pass
        
# mi_coche = Automovil()
# mi_coche.acelerar()
# mi_perro = Perro('Toby', 16, 3)
# print(mi_perro)

#HERENCIA EXTENDIDA 1

# class Padre():
#     def trabajar(self):
#         print("Trabajando en el Hospital")

#     def reir(self):
#         print("Ja ja ja!")

# class Madre():
#     def trabajar(self):
#         print("Trabajando en la Fiscalía")
        
# class Hija(Madre, Padre):
#     pass

# Petra = Hija()
# Petra.trabajar()
# Petra.reir()

# #Herencia extendida 2

# class Vertebrado:
#     vertebrado = False

# class Ave(Vertebrado):
#     tiene_pico = True
#     def poner_huevos(self):
#         print("Poniendo huevos")

# class Reptil(Vertebrado):
#     venenoso = True

# class Pez(Vertebrado):
#     def nadar(self):
#         print("Nadando")
#     def poner_huevos(self):
#         print("Poniendo huevos")

# class Mamifero(Vertebrado):
#     def caminar(self):
#         print("Caminando")
#     def amamantar(self):
#         print("Amamantando crías")

# class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
#     pass

# ramon = Ornitorrinco()
# ramon.poner_huevos()
# ramon.nadar()
# ramon.amamantar()
# ramon.caminar()
# print(f"El ornitorrinco es un animal {'vertebrado' if ramon.vertebrado else 'No vertebrado'}")
# print(ramon.tiene_pico)
# print(ramon.venenoso)

#Herencia extendida 3

# class Padre():
#     color_ojos = "marrón"
#     tipo_pelo = "rulos"
#     altura = "media"
#     voz = "grave"
#     deporte_preferido = "tenis"
#     def reir(self):
#         return "Jajaja"
#     def hobby(self):
#         return "Pinto madera en mi tiempo libre"
#     def caminar(self):
#         return "Caminando con pasos largos y rápidos"
        
# class Hijo(Padre):
#     def hobby(self):
#         return "Juego videojuegos en mi tiempo libre."
    
# peter = Hijo()
# print(peter.hobby())

#POLIFORMISMO 1

# palabra = "polimorfismo"
# lista = ["Clases", "POO", "Polimorfismo"]
# tupla = (1, 2, 3, 80)

# elementos = [palabra, lista, tupla]

# for elemento in elementos:
#     print(len(elemento))

# #POLIFORMISMO 2

# class Mago():
#     def atacar(self):
#         print("Ataque mágico")
# class Arquero():
#     def atacar(self):
#         print("Lanzamiento de flecha")

# class Samurai():
#     def atacar(self):
#         print("Ataque con katana")
        
# Arquero1 = Arquero(); Mago1 = Mago(); Samurai1 = Samurai()
# personajes = [Arquero1, Mago1, Samurai1]

# for personaje in personajes:
#     personaje.atacar()
    
#POLIFORMISMO 3

# class Mago():
#     def defender(self):
#         print("Escudo mágico")

# class Arquero():
#     def defender(self):
#         print("Esconderse")

# class Samurai():
#     def defender(self):
#         print("Bloqueo")

# Arquero2 = Arquero(); Mago2 = Mago(); Samurai2 = Samurai()

# def personaje_defender(personaje):
#     personaje.defender()
    
# personaje_defender(Mago2)

#MÉTODOS ESPECIALES 1

# class Libro():
#     def __init__(self, titulo, autor, cantidad_paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.cantidad_paginas = cantidad_paginas
        
#     def __str__(self):
#         return f'"{self.titulo}", de {self.autor}'

# libro1 = Libro('100 años de soledad', 'Gabriel García Márquez', 448)
# print(libro1)

#MÉTODOS ESPECIALES 2

# class Libro():
#     def __init__(self, titulo, autor, cantidad_paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.cantidad_paginas = cantidad_paginas

#     def __len__(self): #sólo vale para valores enteros 
#         return self.cantidad_paginas

# donQuijote = Libro('El Quijote', 'Miguel de Cervantes', 1300)
# print(len(donQuijote))

#MÉTODO ESPECIAL 3

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print('Libro eliminado')
    
libro1 = Libro('Invisible', 'Eloy Moreno', 378)
print(libro1)
del libro1
# print(libro1)

        
