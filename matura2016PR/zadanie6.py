def szyfruj_znak(z, k):
    kod_znaku = ord(z) + k
    while kod_znaku > 90:
        kod_znaku -=26
    return chr(kod_znaku)

def szyfruj_slowo(s, k):
    szyfr = ' '
    for z in s:
        szyfr = szyfr + szyfruj_znak(z, k)
    return szyfr

# 6.1
k = 107
szyfrogram = ' '
with open("dane_6_1.txt", 'r') as dane:
    for slowo in dane:
        slowo = slowo.strip()
        szyfrogram = szyfrogram + szyfruj_slowo(slowo, k) + "\n"
with open("wyniki_6_1.txt", 'w') as w:
    w.write(szyfrogram)

# 6.3
bledy = ' '
with open("dane_6_3.txt", 'r') as dane:
    for d in dane:
        d = d.strip()
        slowo = d.split(" ")
        z = slowo[0][0]
        z_z = slowo[1][0]
        k = ord(z_z) - ord(z)

        #if slowo[1] != szyfruj_slowo(slowo[0], )

with open("wyniki_6_3.txt", 'w') as w:
    w.write(bledy)
