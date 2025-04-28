def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")
    
try:
    # Código que queremos probar
    suma()

except TypeError:
    #Codigo a ejecutar si hay un error
    print("Estás concatenando tipos distintos")
    
except ValueError:
    print("Has ingresado algún valor que no es un número")

else: 
    #Codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
    
finally:
    #Código que se va a ejecutar de todos modos
    print("Eso fue todo")
    
# def pedir_numero():
    
#     while True:
#         try:
#             numero = int(input("Dame un numero: "))
#         except:
#             print("Ese no es un número.")
#         else:
#             print(f"Ingresate el número {numero}")
#             break
#     print("Recibido número.")

# pedir_numero()
            
    