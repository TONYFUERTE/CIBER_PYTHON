class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir (self):
        print('jajajaja')
    
    def hablar(self):
        print('Ponte una chaquetita')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
print(mi_nieto.hablar())
print(Nieto.__mro__) #method order resolution

