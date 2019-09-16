wynik1 = 0
wynik2 = []
liczby = []
potegi = []
n = 1
while n < 100_000:
    potegi.append(n)
    n *= 3

def czy_potega(n):
    n = int(n)
    if n in potegi:
        return True
    else:
        return False


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

def suma_silni(n):
    suma = 0
    n = str(n)
    for l in n:
        suma += silnia(int(l))
    if suma == int(n):
        return True
    else:
        return False

def NWD(*a):
    d = 1
    for i in range(min(a), 1, -1):
        d = i
        for c in a:
            if c % i != 0:
                d = 1
        if d > 1:
            break
    return d

liczba2 = 1
with open("Dane_PR2/liczby.txt","r") as plik:
    for liczba in plik:
        liczba = liczba.strip()
        liczby.append(int(liczba))
        if czy_potega(liczba):
            wynik1 += 1
        if suma_silni(liczba):
            wynik2.append(liczba)

def pop(list):
    if NWD(*list) < 2:
        print("pop - ",list[0])
        list.pop(0)
        pop(list)
    elif NWD(*list) > 1:
        return list

nwd = 1
dl = 1
pier = 0
a0 = 0
b = []
k = 0

for i in range(len(liczby) - 1):
    k = i + 1
    b = [liczby[i], liczby[k]]
    while NWD(*b) > 1:
        nwd = NWD(*b)
        if k < len(liczby):
            k += 1
            b.append(liczby[k])
        else:
            break

    if len(b) > dl:
        dl = len(b) - 1
        a0 = b[0]

    b.append(liczby[i])

with open('wyniki4.txt', 'w') as w:
    w.write("4.1\n" + str(wynik1) + '\n')
    w.write("4.2\n" + str(wynik2) + '\n')
    w.write("4.1\n" + str(a0) +' '+ str(dl) +' '+ str(nwd) + '\n')