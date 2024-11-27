class Pajaro: 
    
    alas = True 
    
    def __init__(self, color, especie):      #Constructor para darle atributos 
        self.color = color
        self.especie = especie
        
    def piar(self):                            #métodos de nuestra clase
        print('pio')
        
    def volar(self, metros):
        print(f'Ha volado {metros} metros')
        self.piar()                 #Métodos de instancia pueden acceder a otros métodos
        
    def pintar_negro(self):       #Métodos de instancia. Acceden y modifican atributos del objeto
        self.color = 'negro'
        print(f"Ahora el pájaro es {self.color}")
     
#MÉTODOS DE CLASE   
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False      #Si puedes cambiar los atributos de clase
        cls.color = 'Rojo'
        print(Pajaro.alas, Pajaro.color)
        
#MÉTODOS ESTÁTICOS. No pueden modificar los atributos de una instancia ni de una clase.
    @staticmethod
    def mirar():
        print('El pájaro mira')
        
    
Pajaro.poner_huevos(3)
# Pajaro.piar() #No se puede hacer con los otros métodos. 
Pajaro.mirar()