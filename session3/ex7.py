"""
    Ex. 7: Scrieti o functie care sa primeasca trei parametri
        - prefix (string)
        - word (string)
        - suffix (string)
    Si trebuie sa intoarca cuvantul cu prefixul si sufixul adaugate.

    Raspuns:
        - pentru prefix = 'a', suffix = 'b' si word = 'x'
            ---> 'axb'

    Observatii:
        - functia trebuie sa aiba MAXIM 1 linie de cod ca si body
"""
def add_pref_str_suff(prefix, word, suffix):
    return prefix + word + suffix

prf = input('Introduceti un prefix:')
wrd = input('introduceti  un sir de caractere:')
suf = input('Introduceti un sufix:')

print(add_pref_str_suff(prf, wrd, suf))
