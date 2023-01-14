def paaohjelma():
    luku1 = 0
    luku2 = 0
    luvut = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(luvut, "r")
    talleta = open("L06T5T1.txt", "w")
    while True:
        valikko()
        toiminto = int(input("Valitse toiminto (0-3): "))
        if toiminto == 1:
            luku1 = LueLuku(tiedosto)
            luku2 = LueLuku(tiedosto)
            print("Luettiin luvut {0} ja {1}".format(luku1, luku2))
        elif toiminto == 2:
            Summa(talleta,luku1,luku2)
        elif toiminto == 3:
            Osamaara(talleta,luku1, luku2)
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

def LueLuku(tiedosto):
    rivi = tiedosto.readline()
    luku = rivi[:-1]
    if luku == "":
        print("Luvut loppuivat, lopeta ohjelma.")
        return 0
    return luku

def Summa(talleta, luku1, luku2):
    summa = int(luku1)+int(luku2)
    talleta.write("Summa {0} + {1} = {2}\n".format(luku1, luku2, summa))
    print("Tulos tallennettu tiedostoon.")

def Osamaara(talleta, luku1, luku2):
    if luku2 != 0:
        talleta.write("Osamäärä {0} / {1} = {2}\n".format(luku1, luku2, round(int(luku1)/int(luku2),2)))
        print("Tulos tallennettu tiedostoon.")
    else:
        print("Nollalla ei voi jakaa.")

paaohjelma()