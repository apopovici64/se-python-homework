"""
    Ex. 14: Creati o functie get_me_numbers, care sa aiba o functie interioara
    multiply_by_5.

    multiply_by_5 primeste un parametru x, si il inmulteste cu 5, si intoarce
    rezultatul.

    get_me_numbers, primeste un parametru x, adauga 5 si apoi se foloseste
    de multiply_by_5 pentru a il inmulti cu 5, iar la final, mai adauga 3.

    Exemplu:
        daca apelez get_me_numbers(3)
            --> (3 + 5) * 5 + 3 = 43
"""
def get_me_numbers(x):
    def multiply_by_5(y):
        res = y * 5
        return res
    result = multiply_by_5(x+5) + 3
    #print(result)
    return result

get_me_numbers(3)