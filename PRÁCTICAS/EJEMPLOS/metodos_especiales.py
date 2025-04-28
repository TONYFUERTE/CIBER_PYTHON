class CD:
    
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    
    def __str__(self): 
        return f"Album: {self.titulo} de {self.autor}"
    """--str-- definir la forma en la que quiero que 
    se manifieste un string de la clase"""
    
    def __len__(self):   #sólo vale para darnos los valores enteros
        return self.canciones
    
    def __del__(self):
        print('Vas a eliminar la instancia de la clase.')
    

mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)


# print(len(texto))
print(len(mi_cd))

del mi_cd #para eliminar el objeto
