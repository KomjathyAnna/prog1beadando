from itertools import product, islice


def szamok(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)


def generalt():
    m_jelek = ['+', '-', '']
    return [szamok(p) for p in product(m_jelek, repeat=9) if p[0] != '+']


def osszes_szam():
    ertekek = {}
    for szamok in generalt():
        ertek = eval(szamok)
        if ertek not in ertekek:
            ertekek[ertek] = 1
        else:
            ertekek[ertek] += 1
    return ertekek


def szamol(ertek):
    for s in filter(lambda x: x[0] == ertek, map(lambda x: (eval(x), x), generalt())):
        print(s)

szamol(100)
