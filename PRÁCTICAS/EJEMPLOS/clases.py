class Pajaro: 
    pass

mi_pajaro = Pajaro() #Tengo una instancia a la clase Pajaro
otro_pajaro = Pajaro() #Otra instancia.
# print(type(mi_pajaro))
# print(mi_pajaro)
# print(otro_pajaro)

class Casa:
    
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa('blanco', 4)
print(f' La casa blanca es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos.' )


class Cubo:
    caras = 6
    
    def __init__(self, color):
        self.color = color
        
cubo_rojo = Cubo('Rojo')
        
class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
    
    def hechizo (self):
        print('Hada Cadabra!!!!!!!')
    
    def transformar_especie (self):
        self.especie = 'lechuza'
        
    @classmethod
    
    def mana (cls, magia):
        print(f'La nueva magia es {magia}')
        cls.real = True
    
    

# Harry_Potter = Personaje('humano', True, 17)
# Harry_Potter.hechizo()
# Harry_Potter.transformar_especie()
# print(Harry_Potter.especie)
Personaje.mana('lo que sea')

        


