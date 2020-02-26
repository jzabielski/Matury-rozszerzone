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

licznik1 = 0
for dzialka1 in dzialki:
    if trawa(dzialka1):
        licznik1 += 1

for i in range(49):
    for k in range(49):
        if k != i:
            if symetria(dzialki[i],dzialki[k]):
                print(k+1, i+1)
                break