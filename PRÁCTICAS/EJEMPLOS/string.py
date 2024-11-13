from inspect import currentframe as nu
from inspect import getframeinfo as get

n1 = "Euge"
n2 = "nio"
print(get(nu()).lineno, n1 + n2) #Los string se pueden sumar #  type: ignore
print(get(nu()).lineno, n1 * 10) #multiplicarlos
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""

#incluido o no 
print(poema);
print(get(nu()).lineno, "color" in poema) #Devuelve True si la encuentra 
print(get(nu()).lineno,end=": "); print( "sol" in poema) #Devuelve False si no la encuentra 
print(get(nu()).lineno,end=": "); print( "sol" not in poema) #Devuelve true si no la encuentra 

#Numero de línea
print(get(nu()).lineno,end=": ");    print(len(poema))
print(get(nu()).lineno,end=": ");    print(len("agua"))
