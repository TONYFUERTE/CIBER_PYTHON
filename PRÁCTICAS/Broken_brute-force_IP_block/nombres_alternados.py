
print("############################NOMBRES DE USUARIO###########################3")
for i in range(150):
    if i % 3:
        print("carlos")
    else:
        print("wiener")

print("###########################PASSWORDS######################################")
with open ('C:/Users/admin/Documents/PUK/PYTHON/Repositorio/PRÁCTICAS/Broken_brute-force_IP_block/passwords.txt', 'r') as f: 
    lines = f.readlines()

#print(lines)

i=0
for pwd in lines: 
    if i % 3:
        print(pwd.strip('\n'))
    else:
        print('peter')
        print(pwd.strip('\n'))
        i += 1
    i += 1    
 
    