"""
Zadanie 6 matura 2017PR
(C) Patryk Ragus, listopad 2019r.
Lo w Sobolewie
"""
najjasniejszy = 0
najciemniejszy = 255
nie_symetryczne = 0

with open("dane.txt", 'r') as dane:
    for px in dane:
        px = px.strip()
        piksel = px.split(" ")
        for pk in piksel:
            pk = int(pk)
            if pk > najjasniejszy:
                najjasniejszy = pk
            if pk < najciemniejszy:
                najciemniejszy = pk

        if  piksel != piksel [::-1]:
            nie_symetryczne += 1


with open("wyniki6.txt", 'w') as plik:
    plik.write("6.1\n"
                    + "najciemniejszy: "
                    + str(najciemniejszy)
                    + "\nnajjasniejszy: "
                    + str (najjasniejszy)
                    + "\n6.2\n"
                    + str(nie_symetryczne))



