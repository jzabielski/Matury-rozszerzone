def rosnaca(n):
    czy_rosnaca = True
    i = 0
    for k in str(n):
        if int(k) < i:
            czy_rosnaca = False
        i = int(k)
    return czy_rosnaca

wynik1 = 0
wynik2 = 0
liczby = []
with open("Dane_PR/dane.txt",'r') as plik:
    for line in plik:
        line = line.strip()
        if line[0] == line[-1]:
            wynik1 += 1
        d = str(int(line, 8))
        if d[0] == d[-1]:
            wynik2 += 1
        if rosnaca(line):
            liczby.append(line)
max = 0
min = 200000000
for l in liczby:
    l = int(l)
    if l > max:
        max = l
    if l < min:
        min = l


print(wynik1)
print(wynik2)
print(len(liczby))
print(max)
print(min)

with open("wyniki6.txt",'w') as w:
    w.write("a)\n"+ str(wynik1)+"\n"
            + "b)\n"+str(wynik2)+"\n"
            + "c)\n"+str(len(liczby))+"\n"
            + str(min) + "\n" + str(max)+"\n")