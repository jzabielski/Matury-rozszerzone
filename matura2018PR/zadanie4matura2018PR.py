"""
Zadanie 4 matura 2018 PR
(C) Jarosław Zabielski, październik 2019
LO w Sobolewie
"""
przeslanie = ""
i = 0
with open("sygnaly.txt", "r") as plik:
    for sygnal in plik:
        i += 1
        sygnal = sygnal.strip()
        print(sygnal)
        if i%40 == 0:
            przeslanie = przeslanie + sygnal[9]

with open("wyniki4.txt", "w") as wyniki:
    wyniki.write("4.1\n" +
                 przeslanie + "\n")