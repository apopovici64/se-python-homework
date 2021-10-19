"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""
def add_1_to_string(str1):
    return ''.join(chr(ord(char) + 1) for char in str1)

str1 = input('Introduceti un sir de caractere:')
print(add_1_to_string(str1))
