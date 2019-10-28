"""
Matura 2019 zadanie 4
(C) Damian Kopik LO Sobolew
wrześen
"""
licznik1 = 0
potegi = []
nwd_tmp = 0
def silnia(n):
    if n == 0:
        return 1
    else:
        return n*1*silnia(n-1)
def suma_silnia(n):
    suma = 0
    for cyfra in n:
        suma += silnia(int(cyfra))
    return suma
def NWD(a*):
    d = 1
    for c in range(1,min(a)):
        d = 1
        for c in a:
            if c % i != 0:
                d = 1


with open("przyklad.txt",'r') as plik:
    for i in plik:
        print(int(i.strip()))
        if suma_silnia(i) == int(i):
            z4_2 = z4_2 + i + "\n"

        i = int(i)
        if i in potegi:
            licznik1 += 1
for i in range(len(a) - 1):
    k = i+1
    b = [a[i],a[k]]
    while NWD(*b) > 1:
        nwd_tmp = NWD(*b)
        if k < len(a):
            k += 1
            b.append(a[k])
    else:
        break
if len(b) > d1:
    d1 = len(b)
    a0 = b[0]
    nwd = nwd_tmp


print(licznik1)
with open("wynik4.txt",'w') as wyniki:
    wyniki.write("4.1"+"\n"+str(licznik1)+"\n"+str(licznik1)+"\n"+z4_2+"4.3"+"\n"+str(a0)+"\n"+str(d1)+"\n"+str(nwd))

a = [24,8,16,128]
nwd = NWD(*a)
a0 = a[0]
d1 = len(a)
maximum = max(a)
print(nwd,a0,d1,maximum)
