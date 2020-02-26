tj = []
klucze1 = []
sz = []
klucze2 = []
a = []
b = []
def szyfrowanie_znaku(a, b):
    a = ord(a)
    b = ord(b) - 64
    d = a + b
    while d > 90:
        d -= 26
    return chr(d)

def deszyfrowanie_znaku(a, b):
    a = ord(a)
    b = ord(b) - 64
    d = a - b
    while d < 65:
        d += 26
    return chr(d)

def szyfrowanie_wyrazu(wyraz, klucz):
    szyfrogram = ''
    while len(wyraz) > len(klucz):
        klucz = klucz + klucz
    for i in range(len(wyraz)):
        szyfrogram += szyfrowanie_znaku(wyraz[i],klucz[i])
    return szyfrogram

def deszyfrowanie_wyrazu(szyfrogram, klucz):
    wyraz = ''
    while len(szyfrogram) > len(klucz):
        klucz = klucz + klucz
    for i in range(len(szyfrogram)):
        wyraz += deszyfrowanie_znaku(szyfrogram[i],klucz[i])
    return wyraz

with open("Dane_PR/tj.txt","r") as plik:
    for line in plik:
        line = line.strip()
        tj.append(line)
with open("Dane_PR/klucze1.txt","r") as plik:
    for line in plik:
        line = line.strip()
        klucze1.append(line)
with open("Dane_PR/sz.txt","r") as plik:
    for line in plik:
        line = line.strip()
        sz.append(line)
with open("Dane_PR/klucze2.txt","r") as plik:
    for line in plik:
        line = line.strip()
        klucze2.append(line)

for i in range(len(tj)):
   a.append(szyfrowanie_wyrazu(tj[i],klucze1[i]))
for i in range(len(sz)):
   b.append(deszyfrowanie_wyrazu(sz[i],klucze2[i]))

with open('wynik4a.txt','w') as w:
    for k in a:
        w.write(k + "\n")
with open('wynik4b.txt','w') as w:
    for k in b:
        w.write(k + "\n")