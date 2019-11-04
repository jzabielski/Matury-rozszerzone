najjasniejszy = 0
najciemniejszy = 255
nie_symetryczne = 0
with open("dane.txt",'r') as dane:
    
    for px in dane:
        px = px.strip()
        print(px)
        piksel = px.split(" ")
        #6.1
        for pk in piksel:
            print(pk)
            pk = int(pk)
            if pk > najjasniejszy:
                najjasniejszy = pk
            if pk < najciemniejszy:
                najciemniejszy pk
        #6.2
        if piksel != piksel[::-1]:
            nie_symetryczne + 1
with open("wyniki6.txt",'w') as plik:
    plik.write("6.1\n" + "najciemniejszy:"+str(najciemniejszy)+"najjasniejszy: "+str(najjasniejszy)+ "\n6.2\n"+str(nie_symetryczne) )
