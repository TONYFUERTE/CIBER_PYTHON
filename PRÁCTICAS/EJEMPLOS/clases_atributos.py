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
        
mi_pajaro = Pajaro('negro', 'Tucán')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(mi_pajaro.alas)
mi_pajaro.piar()
mi_pajaro.volar(10)
mi_pajaro.pintar_negro()
print(mi_pajaro.color)

mi_pajaro.alas = False   #También podemos modificar estados de clase
print(mi_pajaro.alas)

print(f'Mi pajaro es un {mi_pajaro.especie} y su color es {mi_pajaro.color}')