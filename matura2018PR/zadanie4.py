"""
Matura 2018PR, zadanie 4
(C) Patryk Ragus
LO w Sobolewie
"""
def RozneLitery(s):
    l_liter = 0
    znaki = []
    for z in s:
        if not z in znak:
            znak.append(z)
    return len(znaki)

alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
def OdlLiter(a, b):
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
            mniej10 = OdlLiter2(z, s[i]) <= 10
            if not mniej10:
                break
    return mniej10

przeslanie = ""
i = 0
wyraz = ""
max_znakow = 0
with open ("sygnaly.txt", 'r') as plik:
    for sygnal in plk:
        i += 1
        sygnal = sygnal.strip()
        if i%40 == 0:
            przeslanie = przeslanie + sygnal[9]
        if RozneLitery(sygnal)
