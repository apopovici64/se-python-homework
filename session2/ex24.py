"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""
x = input("Introduceti un numar intreg:")
x = str(x)
x1 = str(x)
if x1[::0] == x:
    print("x Palindrom: True")
else:
    print("x Palindrom: False")