dane = []
with open("Dane_PR2/dzialki.txt","r") as plik:
    for d in plik:
        d = d.strip()
        dane.append(d)
dzialki = []
dzialka = []

for line in dane:
    if line != "":
        dzialka.append(line)
    else:
        dzialki.append(dzialka.copy())
        dzialka.clear()

def trawa(args):
    trawka = 0
    for rzad in args:
        for znak in rzad:
            if znak == '*':
                trawka += 1
    if (trawka/900)*100 >= 70:
        return True
    else:
        return False

def symetria(d1, d2):
    dd1 = ''
    dd2 = ''
    for rzad in d1:
        dd1 += rzad
    for rzad in d2:
        dd2 += rzad
    if dd1 == dd2[::-1]:
        return True
    else:
        return False

def kwadrat(dzialka):
    bok = 0
    ok = True
    while ok and bok<30:
        for i in range(bok+1):
            if dzialka[i][bok] == "X":
                ok = False
                break
        for i in range(bok+1):
            if dzialka[bok][i] == "X":
                ok = False
                break
        bok += 1
    return bok - 1

licznik1 = 0
zad2 = []
licznik3 = 0
zad3 = []
for dzialka1 in dzialki:
    if trawa(dzialka1):
        licznik1 += 1

for i in range(49):
    kw = kwadrat(dzialki[i])
    if kw > licznik3:
        licznik3 = kw
for i in range(49):
    if kwadrat(dzialki[i]) == licznik3:
        zad3.append(i+1)
for i in range(49):
    for k in range(49):
        if k != i:
            if symetria(dzialki[i],dzialki[k]):
                if k+1 not in zad2:
                    zad2.append(k+1)
                if i+1 not in zad2:
                    zad2.append(i+1)
print(licznik1)
print(zad2)
print(licznik3)
print(zad3)

