"""
Zadanie 4 matura 2018 PR
(C) Jarosław Zabielski, październik 2019
LO w Sobolewie
"""
def RozneLitery(s):
    znaki = []
    for z in s:
        if not z in znaki:
            znaki.append(z)
    return len(znaki)

alfabet = ['A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T',
           'U','V','W','X','Y','Z',]

def OdlLiter1(a, b):
    i = abs(alfabet.index(a) - alfabet.index(b))
    return i

def OdlLiter2(a, b):
    i = abs(ord(a) - ord(b))
    return i

def OdstepMniej10(s):
    mniej10 = True
    dl = len(s)
    for z in s:
        for i in range(dl):
            if OdlLiter2(z, s[i]) > 10:
                mniej10 = False
                break
    return mniej10

przeslanie = ""
i = 0
wyraz = ''
max_znakow = 0
ciag = ''
with open("sygnaly.txt", "r") as plik:
    for sygnal in plik:
        i += 1
        sygnal = sygnal.strip()
        if i%40 == 0:       # 4.1
            przeslanie = przeslanie + sygnal[9]
        # 4.2
        if RozneLitery(sygnal) > max_znakow:
            max_znakow = RozneLitery(sygnal)
            wyraz = sygnal
        # 4.3
        if OdstepMniej10(sygnal):
            ciag = ciag + sygnal + "\n"

with open("wyniki4.txt", "w") as wyniki:
    wyniki.write("4.1\n"
                 + przeslanie
                 + "\n")
    wyniki.write("4.2\n"
                 + str(max_znakow)
                 + "\n"
                 + wyraz
                 + "\n")
    wyniki.write("4.3\n"
                 + ciag
                 + "\n")