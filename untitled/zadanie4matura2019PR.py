#zadanie 4 matura 2019PR
# (C) Karol Kożuchowski, wrzesień 2019 r
# LO W Sobolewie
def NWD(*a):
    d = 1
    for c in range(1, min(a)):
        d = i
        for c in a:
            if c % i != 0:
                d = 1
            if d > 1:
                break
print NWD

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
with open("przyklad.txt", 'r') as plik:
    for i in plik:
        i = (i.strip())
        if suma_silni(i) ==int(i):
            z4_2 = z4_2 + i + "\n"
        i =int(i)
        if i in potegi:
            licznik1 +=1

print(licznik1)
with open("wynik.txt", 'w') as wyniki:
    wyniki.write("4.1" + "\n" + str(licznik1) + "\n"
                 + z4_2)

print(silnia(4))
print(suma_silni("143"))