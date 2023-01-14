toiminto = -1
luku1 = 0
luku2 = 0
while toiminto != 0:
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Erotus")
    print("4) Tulo")
    print("5) Osamäärä")
    print("6) Potenssi")
    print("0) Lopeta")
    toiminto = int(input("Valitse toiminto (0-6): "))
    if toiminto == 0:
        print("Lopetetaan")
    elif toiminto == 1:
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        print("Annoit luvut", luku1, "ja", luku2)
        print("")
    elif toiminto == 2:
	    print("Summa", luku1, "+", luku2, "=", (luku1+luku2))
    elif toiminto == 3:
	    print("Erotus", luku1, "-", luku2, "=", (luku1-luku2))
    elif toiminto == 4:
	    print("Tulo", luku1, "*", luku2, "=", (luku1*luku2))
    elif toiminto == 5:
	    if luku2 ==0:
		    print("Nollalla ei voi jakaa.")
	    else:
		    print("Osamäärä", luku1, "/", luku2, "=", round((luku1/luku2),2))
    elif toiminto == 6:
	    print("Potenssi", luku1, "**", luku2, "=", (luku1**luku2))
    else:
	    print("Tuntematon valinta, yritä uudestaan.")
print("Kiitos ohjelman käytöstä.")