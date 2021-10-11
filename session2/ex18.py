"""
    Veti primi un string de la tastatura.
    Veti primi doua numere intregi de la tastatura, x, y.
    Va trebui sa printati substringul de la indexul x la indexul y (inclusiv).

    exemplu:
        Veti primi: 'Center for Intelligent Machines', 2, 5
        Veti printa: 'nter'
"""
s = input("Introduceti sirul de caractere:")
x, y = [int(a) for a in input("Introduceti doua numere intregi:").split()]
print(s[x:y])