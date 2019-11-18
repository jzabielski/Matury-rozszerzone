def szyforwanie(slowo, n):
    szyfr = ""
    for i in slowo:
        nr = ord(i) + n
        while nr > 90:
            nr -=26
        szyfr += chr(nr)
    return szyfr


odp1 = []
with open('Dane_PR2/dane_6_1.txt','r') as plik:
    for slowo in plik:
        slowo = slowo.strip()
        odp1.append(szyforwanie(slowo,107))

odp3 = []
with open('Dane_PR2/dane_6_3.txt','r') as plik:
    for line in plik:
        zle = 0
        line = line.strip()
        slowo1, slowo2 = line.split()
        if ord(slowo2[0]) > ord(slowo1[0]):
            k = ord(slowo2[0]) - ord(slowo1[0])
        else:
            k = ord(slowo2[0]) - ord(slowo1[0]) + 26
        if szyforwanie(slowo1,k) != slowo2:
            odp3.append(slowo1)

with open('wyniki_6_1.txt','w') as wynik:
    for s in odp1:
        wynik.write(s + '\n')
with open('wyniki_6_2.txt','w') as wynik:
    for s in odp3:
        wynik.write(s + '\n')
