def suma_ASCII(napis):
    suma = 0
    for a in napis:
        suma += ord(a)
    return suma

def pierwsza(n):
    pierwsza = True
    if n == 1:
        pierwsza = False

    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            pierwsza = False
    if n == 2:
        return True
    return pierwsza

def rosnacy(napis):
    rosnacy = True
    k = 0
    for a in napis:
        if ord(a) < k:
            rosnacy = False
        k = ord(a)
    return rosnacy

wynik1 = 0
wynik2 = []
wynik3 = []
wyrazy = []
with open("dane_PR/NAPIS.txt","r") as plik:
    for line in plik:
        line = line.strip()
        if pierwsza(suma_ASCII(line)):
            wynik1 += 1
        if rosnacy(line):
            wynik2.append(line)
        wyrazy.append(line)

for i in range(len(wyrazy)):
    for j in range(len(wyrazy)):
        if i != j and wyrazy[i] == wyrazy[j]:
            if wyrazy[i] not in wynik3:
                wynik3.append(wyrazy[i])
print(wynik3)


with open("ZADANIE5.txt","w") as wyniki:
    wyniki.write("a)\n" + str(wynik1) + "\n" + "b)\n")
    for n in wynik2:
        wyniki.write(n + "\n")
    wyniki.write("c)\n")
    for k in wynik3:
        wyniki.write(k + "\n")