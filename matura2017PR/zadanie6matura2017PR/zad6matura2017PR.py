"""
Zadanie 6 matura 2017 PR
(C) Jarosław Zabielski, listopad 2019
LO w Sobolewie
"""

# 0 - czarny    255 - biały
najjasniejszy = 0
najciemniejszy = 255
nie_symetryczne = 0
p = [1,2,3,4,5]
print(p[2])
with open("dane.txt", 'r') as dane:
    w = 0
    for px in dane:
        px = px.strip()
        piksel = px.split(" ")
        #6.1
        k = 0
        for pk in piksel:
            pk = int(pk)
            #p[k][w] = pk
            if pk > najjasniejszy:
                najjasniejszy = pk
            if pk < najciemniejszy:
                najciemniejszy = pk
            k += 1
        w += 1
        #6.2
        if piksel != piksel[::-1]:
            nie_symetryczne += 1

with open("wyniki6.txt","w") as plik:
    plik.write("6.1\n"
               + "najciemniejszy: "
               + str(najciemniejszy)
               + "\nnajjasniejszy: "
               + str(najjasniejszy)
               + "\n6.2\n"
               + str(nie_symetryczne))
