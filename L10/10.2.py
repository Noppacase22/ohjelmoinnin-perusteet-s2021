######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 15.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import sys

def paaohjelma():
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    kirja = lue(tiedostonimi)
    analysoi(kirja)
    print("Kiitos ohjelman käytöstä.")

def lue(tiedostonimi):
    kirjasto = {}
    try:
        tiedosto = open(tiedostonimi, "r", encoding="utf-8")
        tiedosto.readline()
        for rivi in tiedosto:
            auto = rivi.split(";")
            try:
                kirjasto.update({auto[1][:4] : kirjasto.get(auto[1][:4])+1})
            except Exception:
                kirjasto.update({auto[1][:4] : 1})    
        return kirjasto
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def analysoi(kirja):
    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")
    lista = sorted(kirja)
    lista.reverse()
    a = 0
    for avain in lista:
        print(f"{avain}: {kirja.get(avain)}")
        a += kirja.get(avain)
    print(f"Yhteensä {a} autoa.")

paaohjelma()