from colored import fg, bg, attr

color = fg(1) + bg(15)
print(color + 'Texto con color' + attr(0))



from openpyxl import *