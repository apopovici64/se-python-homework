"""
    Veti primi un string de la tastatura.
    Veti primi un intreg de la tastatura, x.
    Va trebui sa printati acel string, concatenat de x ori.

    exemplu:
        Veti primi: 'cmi', 5
        Veti printa: 'cmicmicmicmicmi'
"""
str = input("Introduceti sirul de caractere:")
x = input("Introduceti nr intreg:")
x = int(x)
output = ''
for i in range(x):
    output += str
print(output)