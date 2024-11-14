class Pajaro: 
    
    alas = True 
    
    def __init__(self, color, especie):      #Constructor para darle atributos 
        self.color = color
        self.especie = especie
        
    def piar(self):                            #métodos de nuestra clase
        print('pio')
        
    def volar(self, metros):
        print(f'Ha volado {metros} metros')
        
mi_pajaro = Pajaro('negro', 'Tucán')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(mi_pajaro.alas)
mi_pajaro.piar()
mi_pajaro.volar(10)


print(f'Mi pajaro es un {mi_pajaro.especie} y su color es {mi_pajaro.color}')