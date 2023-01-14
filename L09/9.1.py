######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 08.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import sys

def paaohjelma():
    paalista = LueTiedosto()
    TallennaTiedosto(paalista)
    print("Kiitos ohjelman käytöstä.")   

def LueTiedosto():
    lista = []
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "r")
        i = 0
        for rivi in tiedosto.readlines():
            i += 1
            lista.append(rivi)
        print(f"Tiedoston '{tiedostonimi}' lukeminen onnistui, {i} riviä.")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista

def TallennaTiedosto(lista):
    tiedostonimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "w")
        i = 0
        for i in range(len(lista)):
            tiedosto.write(lista[i])
            i += 1
        print(f"Tiedoston '{tiedostonimi}' kirjoittaminen onnistui.")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

paaohjelma()