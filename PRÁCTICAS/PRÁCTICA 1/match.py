#MATCH POR IF

serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print('No coincide con ninguna marca.')
    
match serie:    
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print('No coincide con ninguna marca.')


#MATCH CON DICCIONARIOS: 

cliente = {'nombre': 'Manolo',
           'edad': 45,
           'ocupacion': 'mecánico'}

pelicula = {'titulo': 'Matrix',
            'ficha':{'protagonista': 'Keano Reave',
                     'director': 'Lana y Lilly Wachowski'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos: 
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('CLIENTE: ')
            print(nombre, edad, ocupacion)
        case {'titulo':titulo,
              'ficha':{'protagonista': protagonista,
                       'director': director}}:
            print('PELÍCULA:  ')
            print(titulo, protagonista, director)
        case 'libro':
            print('Sólo sabemos que es un libro')
        case _:
            print('No tenemos valores')