######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 18.10.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def paaohjelma():
    luvut = input("Anna luettavan tiedoston nimi: ")
    kirjoita = input("Anna kirjoitettavan tiedoston nimi: ")
    tuloslista = valikko(luvut)
    kirjaa(kirjoita,tuloslista)
    print("Kiitos ohjelman käytöstä.")
    return

def kirjaa(tiedosto,tuloslista):
    tallenna = open(tiedosto, "w")
    for rivi in tuloslista:
        tallenna.write(rivi)
    print(f"Tallennettu tiedosto '{tiedosto}'.")
    tuloslista.clear()

def valikko(luvut):
    luettu = 0
    listaus = []
    while True:
        print("Tämä laskin osaa seuraavat toiminnot:")
        print("1) Anna luvut")
        print("2) Summa")
        print("3) Osamäärä")
        print("0) Lopeta")
        toiminto = input("Valitse toiminto (0-3): ")
        if toiminto == "1":            
            if luettu == 0:
                tiedosto = open(luvut, "r")
                lista = LueLuku(tiedosto)
                print(f"Luettu tiedosto '{luvut}'.")
                luettu = 1
            if lista == []:
                print("Luvut loppuivat, lopeta ohjelma.")
            else:
                luku1 = lista.pop()
                luku2 = lista.pop()
                print("Luettiin luvut {0} ja {1}".format(luku1, luku2))
        elif toiminto == "2":
            listaus.append(Summa(luku1,luku2))
        elif toiminto == "3":
            listaus.append(Osamaara(luku1, luku2))
        elif toiminto == "0":
            return listaus
        else:
            print("Tuntematon valinta, yritä uudestaan.")

def LueLuku(tiedosto):
    lista = []
    for rivi in tiedosto.readlines():
        luku = rivi[:-1]
        lista.append(luku)
    lista.reverse()
    return lista

def Summa(luku1, luku2):
    summa = int(luku1)+int(luku2)
    print("Tulos lisätty listaan.")
    return ("Summa {0} + {1} = {2}\n".format(luku1, luku2, summa))

def Osamaara(luku1, luku2):
    if luku2 != 0:
        print("Tulos lisätty listaan.")
        return ("Osamäärä {0} / {1} = {2}\n".format(luku1, luku2, round(int(luku1)/int(luku2),2)))
    else:
        print("Nollalla ei voi jakaa.")

paaohjelma()