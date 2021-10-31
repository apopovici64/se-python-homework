"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.

    Exemplu:
        la prima rulare, x = 3, stringul generat = 'cmi', fisierul arata asa:
            cmi
        la a doua rulare, x = 6, stringul generat = 'cmicmi', fisierul arata:
            cmi
            cmicmi
        la a treia rulare, x = 1, stringul generat = 'b', fisierul arata asa:
            cmi
            cmicmi
            b
"""

import random

def dec(func):
    def wrapper(*args):
       
        log_file = open("output17.data", "a")
        saving_var = f'{func(*args)}'
        log_file.write(f'\n{saving_var}')
        log_file.close

    return wrapper


# decorate me
@dec
def f(x):
    result = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=x))
    return result

x = input()
x = int(x)

f(x)
