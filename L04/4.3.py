summa = 0
arvo = 0
tosi = 1
while tosi == 1:
	arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa))"))
	if arvosana == -1:
		tosi = 0
	elif 0 < arvosana < 6:
		summa = summa = arvosana
		arvo = arvo + 1
	else:
		print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
print("Arvosanojen keskiarvo on " + round(summa/arvo, 2) + ".")
print("Kiitos ohjelman käytöstä.")