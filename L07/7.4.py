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

class AUTO():
    merkki = ""
    hinta = 0


def paaohjelma():
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    lista = []
    while True:
        print("Käytettävissä olevat toiminnot:\n1) Anna auton tiedot\n2) Tulosta autojen tiedot\n0) Lopeta")
        valinta = int(input("Valintasi: "))
        if valinta == 1:
            auto = AUTO()
            auto.merkki = input("Anna auton merkki: ")
            auto.hinta = input("Anna auton hinta: ")
            lista.append(auto)
        elif valinta == 2:
            print("Listalta löytyy seuraavat automerkit ja hinnat:")
            for auto in lista:
                print(auto.merkki, auto.hinta)
        elif valinta == 0:
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()