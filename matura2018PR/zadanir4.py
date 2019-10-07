a = ''
b1 = 0
b2 = ""
c = []
def rozne_litery(w):
    znaki = []
    for z in w:
        if not z in znaki:
            znaki.append(z)
    return len(znaki)

alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def odleglosc(a,b):
    i = abs(alfabet.index(a) - alfabet.index(b))
    return i

with open('Dane_PR2/sygnaly.txt','r') as file:
    i = 0
    for line in file:
        line = line.strip()
        i+=1
        if i % 40 == 0:
            a += line[9]
        if rozne_litery(line) > b1:
            b1 = rozne_litery(line)
            b2 = line
        k = 0
        for z in line:
            for s in line:
                if odleglosc(z,s) > 10:
                    k = 1
        if k == 0:
            c.append(line)
print(a)
print(b1," ",b2)
print(c)
with open('wyniki4.txt','w') as w:
    w.write('4.1\n' + str(a) + '\n')
    w.write('4.2\n' + str(b1) + '\n' + str(b2) + '\n')
    w.write('4.3\n')
    for napis in c:
        w.write(str(napis) + '\n')