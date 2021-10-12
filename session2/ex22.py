"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
s = input("Introduceti sirul de caractere:")
for i in len(s):
    if i % 2 == 1:
        s[i].upper()
print(s)