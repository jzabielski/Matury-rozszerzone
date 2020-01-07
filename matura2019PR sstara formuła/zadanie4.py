dzialki = []
with open('Dane_PR2/przyklad.txt','r') as plik:
    licznik = 1
    dzialka = []
    for line in plik:
        line = line.strip()
        dzialka.append(line)
        if licznik % 31 == 0:
            dzialki.append(dzialka)
            dzialka = []
            
        licznik += 1

zad1 = 0
zad2 = []

dzialki_w_paskach = []
for i, dzialka in enumerate(dzialki):
    trawa = 0
    pasek = ''
    for linia in dzialka:
        trawa += linia.count('*')
        pasek += linia
    if trawa >= 630:
        zad1 += 1
    dzialki_w_paskach.append(pasek)
    pasek = ''
 
                    
    

for i, dzialka1 in enumerate(dzialki_w_paskach):
    for k, dzialka2 in enumerate(dzialki_w_paskach):
        if dzialka1 == dzialka2[::-1]:
            zad2.append(i+1)
            zad2.append(k+1)
            break
print(zad1)
print(zad2)

