######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 01.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import L08T5Kirjasto

def paaohjelma():
    tiedosto = input("Anna luettavan tiedoston nimi: ")
    toinen = input("Anna kirjoitettavan tiedoston nimi: ")
    oliolista = []
    while True:
        valinta = valikko()
        if valinta == "0":
            break
        elif valinta == "1":
            oliolista = L08T5Kirjasto.LueTiedosto(tiedosto)
        elif valinta == "2":
            L08T5Kirjasto.Varastoi(oliolista)
        elif valinta == "3":
            L08T5Kirjasto.TalletaTiedosto(toinen, oliolista)
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print()
    print("Kiitos ohjelman käytöstä.")

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    return input("Valintasi: ")

paaohjelma()