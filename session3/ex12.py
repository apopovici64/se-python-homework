"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""
def dec(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        b = open("output12.data", "a")
        b.write(str(func(*args, **kwargs)))
        b.close
    return wrapper

# decorate me
@dec
def f(x):
    print(x)

f(3)
