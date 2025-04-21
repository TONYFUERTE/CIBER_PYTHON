class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print(f'Este animal ha nacido, es de color {self.color} estará en cautividad hasta {self.edad} ')
    
    def hablar(self):
        print('Este animal emite un sonido')
        
class Pajaro(Animal):
    def __init__(self, edad, color,altura_vuelo):
        #usamos el método super para llamar a todos los atributos heredados.
        super().__init__(edad, color)    
        self.altura_vuelo = altura_vuelo #añadimos una nueva variable de instancia.
    
    def hablar(self):  #método heredado y modificado
        print("pio")
        
    def volar(self, metros): #nuevo método de la clase Pájaro.
        print(f"El pájaro vuela {metros} metros")

print(Pajaro.__bases__)
print(Animal.__subclasses__)

piolin = Pajaro(2, 'amarillo', 60)
piolin.hablar()  #Ejecuta el método hablar de Pájaro.. 
piolin.volar(100)