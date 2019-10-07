#Dawid Trojanowski
def RozneLitery(s):
	l_liter = 0
	znaki = []
	for z in s:
		if not z in znak:
			znak.append(z)
	return len(znaki)
alfabet = ["","","","","","","","","","",]
def OdLiter(a,b):
	i = abs(alfabet.index(a)) - alfabet.index(b)
	return i
print(OdLiter('A','D'))
def OdLiter2(a,b):
	

przeslanie = ""
i = 0
wyraz = ""
max_znakow = 0
with open("sygnaly.txt",'r') as plik:
	for sygnal in plik:
		i += 1
		sygnal = sygnal.strip()
		if i % 40 == 0:
			przeslanie = przeslanie + sygnal[9]
		if RozneLitery(sygnal) > max_znakow:
			max_znakow = RozneLitery(sygnal)
			wyraz = sygnal
with open("wyniki4.txt",'w') as wyniki:
	wyniki.write("4.1\n"+przeslanie+"\n")
	wyniki.write("4.2\n"+str(max_znakow)+"\n"+ wyraz+"\n")