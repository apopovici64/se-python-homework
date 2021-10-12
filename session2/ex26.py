"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa printati True (boolean) de fiecare data cand elementul
    primit este par, si False (boolean) de fiecare data cand elemtnul primit
    este impar.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa:
        False
        False
        True
        False
        False
"""
l=[]
x = input("Introduceti un numar intreg:")
while str(x) != 'exit':
    if x % 2 == 0:
        print(True)
    if x % 2 == 1:
        print(False)