def wiecej_zer(n):
    zera = 0
    jedynki = 0
    for z in n:
        if z == '0':
            zera += 1
        if z == '1':
            jedynki += 1
    if zera > jedynki:
        return True
def to_int(n):
    w = 0
    d = 1
    for i in n[::-1]:
        w += int(i) * d
        d *= 2
    return(w)

zad1 = 0
podzielne2 = 0
podzielne8 = 0
najmniejsza = 3 * pow(10,250)
najm_linia = 0
najwieksza = 0
najw_linia = 0
with open('Dane_PR2/liczby.txt','r') as plik:
    i = 0
    for liczba in plik:
        i += 1
        liczba = liczba.strip()
        if wiecej_zer(liczba):
            zad1 += 1
        d = len(liczba)
        if liczba[d-1:] == '0':
            podzielne2 += 1
        if liczba[d-3:] == '000':
            podzielne8 += 1
        
        if int(liczba) > najwieksza:
            najwieksza = int(liczba)
            najw_linia = i
        if int(liczba) < najmniejsza:
            najmniejsza = int(liczba)
            najm_linia = i
print(zad1)
print(podzielne2)
print(podzielne8)
print(najm_linia)
print(najw_linia)

