"""
    Ex. 5: Scrieti o functie cu un singur parametru (o lista) care sa
    adauge 1 tuturor elementelor din lista.

    Raspunsul corect:
        - func([1, 2, 3])
            ---> [2, 3, 4]

    Observatii:
        - functia trebuie sa fie MAXIM o linie de cod (2, daca luam in calcul
        si definitia functiei)
        - hint: list comprehensions (google it if you don't know it already)
"""
def  add_1_to_list(list1):
    return [int(x) + 1 for x in list1] # folosim conversia fiecarui caracter din lista  la Integer

list1 = input('Introduceti un set de numare intregi:')
list1 = list(list1) # convertim setul primit (ca string) intr-o lista de caractere
print(add_1_to_list(list1))