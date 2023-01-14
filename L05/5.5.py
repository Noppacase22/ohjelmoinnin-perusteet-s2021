def paaohjelma():
    luku1 = 0
    luku2 = 0
    while True:
        valikko()
        toiminto = int(input("Valitse toiminto (0-3): "))
        if toiminto == 1:
            luku1,luku2 = AnnaLuku()
        elif toiminto == 2:
            Summa(luku1,luku2)
        elif toiminto == 3:
            Osamaara(luku1, luku2)
        elif toiminto == 0:
            print("Lopetetaan")
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    return

def valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    return

def AnnaLuku():
    luku = int(input("Anna ensimmäinen luku: "))
    toinen = int(input("Anna toinen luku: "))
    print("Annoit luvut", luku, "ja", toinen)
    return luku,toinen

def Summa(luku1, luku2):
    print("Summa", luku1, "+", luku2, "=", luku1+luku2)

def Osamaara(luku1, luku2):
    if luku2 != 0:
        print("Osamäärä", luku1, "/", luku2, "=", round(luku1/luku2,2))
    else:
        print("Nollalla ei voi jakaa.")

paaohjelma()