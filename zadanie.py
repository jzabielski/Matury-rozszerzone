screen = []
sasiedzi = 0
with open('dane.txt','r') as plik:
    for line in plik:
        line = line.strip()
        row = line.split(" ")
        screen.append(list(map(int, row)))

for y in range(200):
    for x in range(320):
        s = 0
        if x > 0 and abs(screen[y][x] - screen[y][x-1]) > 128:
            s = 1
        if x < 319 and abs(screen[y][x] - screen[y][x+1]) > 128:
            s = 1
        if y > 0 and abs(screen[y][x] - screen[y-1][x]) > 128:
            s = 1
        if y < 199 and abs(screen[y][x] - screen[y+1][x]) > 128:
            s = 1
        sasiedzi += s

naj = 0
for x in range(320):
    licznik = 1
    for y in range(199):
        if screen[y][x] == screen[y+1][x]:
            licznik += 1
        else:
            naj = max(naj, licznik)
            licznik = 1
