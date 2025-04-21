class Vaca: 
    def __init__ (self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice Muuuu")
        
class Oveja:
    def __init__ (self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice beeee")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

# vaca1.hablar()
# oveja1.hablar()

animales = [vaca1, oveja1] 

for animal in animales:  #podemos iterar por los métodos hablar() de los objetos.
    animal.hablar()

def animal_habla(animal): #Podemos llamar el método con una función
    animal.hablar()

animal_habla(vaca1);
animal_habla(oveja1)