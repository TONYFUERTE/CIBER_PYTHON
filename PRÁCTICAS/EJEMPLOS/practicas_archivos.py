# texto = open('prueba.txt')
# texto.readline()
# print(texto.readline())
# texto.close()

# texto = open('prueba.txt','a')
# texto.write("""queremos
#             meter
#             más líneas
#             para hacer 
#             la iteración""")
# texto.close()


# texto = open('prueba.txt')
# lista_texto = texto.readlines()
# print(lista_texto[5])
# texto.close()

texto = open('prueba.txt','w')
# texto.write('Nuevo texto')

registro_ultima_sesion = ["Federico\t", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
texto.writelines(registro_ultima_sesion)
texto.close()