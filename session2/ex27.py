"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import string
import random
x = input("Introduceti un numar intreg:")
s = ''
ran = s.random.choice(string.ascii_lowercase + string.digits, k = x)
# Rezultat
print("Stringul aleator este: " + str(ran))