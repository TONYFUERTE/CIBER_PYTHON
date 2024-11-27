class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    
    def nacer(self):
        print(f'Este animal ha nacido, es de color {self.color} estará en cautividad hasta {self.edad} ')
        

class Pajaro(Animal):
    pass

# print(Pajaro.__bases__)
# print(Animal.__subclasses__)

piolin = Pajaro(2, 'amarillo')
piolin.nacer()