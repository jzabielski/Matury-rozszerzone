najjasniejszy = najciemniejszy = 128
symetria = 0
tablica = []
with open("Dane_PR2/dane.txt",'r') as plik:
    for row in plik:
        row = row.strip()
        row = row.split(" ")
        tablica.append(list(map(int, row)))
        for led in row:
            if int(led) > najjasniejszy:
                najjasniejszy= int(led)
            if int(led) < najciemniejszy:
                najciemniejszy = int(led)
        if row != row[::-1]:
            symetria += 1

print(tablica)

sasiedzi = 0

for y in range(200):
    for x in range(320):
        s = 0
        if x > 0 and abs(tablica[y][x] - tablica[y][x-1]) > 128:
            s = 1
        if x < 319 and abs(tablica[y][x] - tablica[y][x+1]) > 128:
            s = 1
        if y > 0 and abs(tablica[y][x] - tablica[y-1][x]) > 128:
            s = 1
        if y < 199 and abs(tablica[y][x] - tablica[y+1][x]) > 128:
            s = 1
        sasiedzi += s


naj = 0
for x in range(320):
    licznik = 1
    for y in range(199):
        if tablica[y][x] == tablica[y+1][x]:
            licznik += 1
        else:
            naj = max(naj, licznik)
            licznik = 1

with open('wyniki6.txt','w') as plik:
    plik.write("6.1\n" + "najciemniejszy: " + str(najciemniejszy)
                                + "\nnajjasniejszy: " + str(najjasniejszy)
                + "\n6.2\n" + str(symetria)
                + "\n6.3\n" + str(sasiedzi)
                + "\n6.3\n" + str(naj))


