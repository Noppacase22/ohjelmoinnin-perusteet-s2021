######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 21.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import HTPerusKirjasto

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    valinta = input("Valintasi: ")
    return valinta

def paaohjelma():
    lista = []
    tuloslista = []
    while True:
        valinta = valikko()
        if valinta == "0":
            break
        elif valinta == "1":
            lista = HTPerusKirjasto.lue()
        elif valinta == "2":
            if lista == []:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                tuloslista = HTPerusKirjasto.analysoi(lista)
                print("Tilastotiedot analysoitu.")
        elif valinta == "3":
            if tuloslista == []:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                HTPerusKirjasto.tallenna(tuloslista)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        print("Anna uusi valinta.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()