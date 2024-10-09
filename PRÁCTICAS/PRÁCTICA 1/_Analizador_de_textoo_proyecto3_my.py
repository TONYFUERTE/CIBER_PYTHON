text = input("Introduzca un texto: ")
letters = input("Introduzla las letras que desea buscar separadas por un espacio: ")
list_letters = letters.lower().split()
text_letters = list(text.lower())

# print(text_letters.count(list_letters))
for list in list_letters:
    print(f'El número de letras {list} es: {text_letters.count(list)}')

print(f'El número de palabras en el texto es: {len(text.split())}')
print(f'La primera letra del texto es: {text[0]} y la última es: {text[-1]}')
words = text.split()
inverse = " ".join(words[::-1])
print(f'Si invertimos el orden el texto sería: "{inverse}"')
print(f'La palabra Python se encuentra en el texto es: {'Python' in words}')
dic = {True:"SÍ", False:"NO"}
bool_Python = 'Python' in words
print(f"La palabra Python '{dic[bool_Python]}' se encuentra en el texto")