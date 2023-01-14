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

import HTTavoiteKirjasto

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("4) Analysoi opiskelijoiden palautusmäärät")
    print("5) Analysoi tuntikohtaiset palautukset")
    print("6) Analysoi aikavälien palautukset")
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
            lista = HTTavoiteKirjasto.lue()
        elif valinta == "2":
            if lista == []:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                tuloslista = HTTavoiteKirjasto.analysoi(lista[2])
                print("Tilastotiedot analysoitu.")
        elif valinta == "3":
            if tuloslista == []:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                tuloslista = HTTavoiteKirjasto.tallenna(tuloslista)
        elif valinta == "4":
            if lista == []:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                HTTavoiteKirjasto.PisteAnalyysi(lista[1])
        elif valinta == "5":
            if lista == []:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                HTTavoiteKirjasto.TuntiAnalyysi(lista)
        elif valinta == "6":
            if lista == []:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                HTTavoiteKirjasto.AikaAnalyysi(lista)  
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        print("Anna uusi valinta.")
    lista.clear()
    tuloslista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()