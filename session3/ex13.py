"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""
def dec(func):
    def wrapper():
        result = func()
        result = result[0].upper() + result[1] + result[2].upper()
        print(result)        
    return wrapper

# decorate me
@dec
def f():
    return 'cmi'

f()