with open ('C:/Users/admin/Documents/PUK/PYTHON/Repositorio/PRÁCTICAS/Broken_brute-force_IP_block/passwords.txt', 'r') as f: 
    lines = f.readlines()

# print(lines)

print('[',end='')
contador = 0
for pwd in lines: 
    if contador:
        print(',',end='')
    print('"' + pwd.strip('\n') + '"',end='')
    contador += 1

print(']')

# print(lines_format)