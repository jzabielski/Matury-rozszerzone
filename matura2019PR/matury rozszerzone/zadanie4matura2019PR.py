
#zadanie 4 matura 2019 PR
# (C) Izabela Lapacz, wrzesień 2019 r.
# LO w Sobolewie
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

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

def suma_silni(n):
    suma = 0
    for cyfra in n:
        suma += silnia(int(cyfra))
    return suma

licznik1 = 0
potegi = []
i = 1
while i < 100_000:
    potegi.append(i)
    i *= 3
z4_2 = "4.2" + "\n"
nwd = 0
a0 = 0
dl = 0
nwd_tmp = 0
a = []
with open("liczby.txt",'r') as plik:
    for i in plik:
        i = i.strip()
        if suma_silni(i)==int(i):
            z4_2 = z4_2 + i + "\n"
        i = int(i)
        a.append(i)
        if i in potegi:
          licznik1 += 1

print(licznik1)

for i in range(len(a) - 1):
    k = i+1
    b = [a[i], a[k]]
    while NWD(*b) > 1:
        nwd_tmp = NWD(*b)
        if k<len(a):
            k+=1
            b.append(a[k])
        else:
            break
    if len(b) > dl:
        dl = len(b) - 1
        a0 = b[0]
        nwd = nwd_tmp

#a=[24,8,16,128]
#nwd = NWD(*a)
#a0 = a[0]
#dl = len(a)
print(nwd, a0, dl)

with open("wyniki4.txt","w") as wyniki:
    wyniki.write("4.1" + "\n"
                 + str(licznik1) + "\n\n"
                 + z4_2 + "\n"
                 + "4.3" + "\n"
                 + str(a0) + "\n"
                 + str(dl) + "\n"
                 + str(nwd))