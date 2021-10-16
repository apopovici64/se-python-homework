"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
x = input("Introduceti secventa de paranteze:")
# Formam doua liste(open, close) cu parantezele ce pot apare in secventa:
open_list = ['(', '[', '{']
close_list = [')', ']', '}']
# Solutia trebuie sa testeze daca fata de o secventa de paranteze  ce apartin listei open_list
# avem o secventa de inchidere corespunzatoare...Adica, daca ultima paranteza din secventa este '[' 
# atunci imediat trebuie sa avem o ']' pentru inchidere, altfel tiparim FALSE.
# Daca perechea este inchisa corect, o excludem din analiza si urmarim ca urmatoarea paranteza sa 
# inchida corect paranteza  anterioara celei ce tocmai a fost exclusa...
# Intregul proces analizat sugereaza folosirea unei stive in definirea algoritmului solutiei (ultima pereche
# corect inchisa este prima eliminata-LIFO-iar testarea continua similar pentru parantezele anterior adaugate in stiva
# cu parantezele de inchidere ulterior adaugate)
# Algoritmul se bazeaza asadar pe  folosirea unei structuri de date speciala, o stiva, ce va fi definita in cod 
stack = [] # stiva definita sub forma unei liste
for char in x:
    if char in open_list:
        stack.append(char) # incarcam lista
    elif char in close_list:
        pos = close_list.index(char) # identificam caracterul de inchidere in lista de inchideri corespunzatoare
        # testam daca avem inchidere corecta cu ultimul caracter de deschidere existent in stiva
        if ((len(stack()>0)) and (open_list[pos]==stack[len(stack)-1])):
            stack.pop() # indepartam ultima pereche inchisa corect
        else:
            print(False)
print(True) # daca am golit intreaga stiva anterior incarcata cu perechi corect inchise, inseamna ca am avut o secventa inchisa corect




    


