# Użyj słowa yield i zrób generator wielokrotności dowolnej liczby


def multiple(liczba):
    mnoznik = 1
    while True:
        yield liczba * mnoznik
        mnoznik += 1

gen = multiple(5)

for x in range(10):
    print(next(gen))
