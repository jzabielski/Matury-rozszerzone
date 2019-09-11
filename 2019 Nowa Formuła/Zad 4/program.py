# Dawid Trojanowski
licznik1 = 0
potegi = []
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
print(licznik1)
with open("wynik4.txt",'w') as wyniki:
    wyniki.write("4.1"+"\n"+str(licznik1)+"\n")

    print(suma_silnia("143"))
