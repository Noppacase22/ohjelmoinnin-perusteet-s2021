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

import numpy

def paaohjelma():
    print("Tämä ohjelma esittelee numpy-matriisin käyttöä.")
    rivit = 4
    sarak = 4
    matriisi = numpy.zeros((rivit, sarak), int)
    for rivi in range(rivit):
        for sarake in range(sarak):
            matriisi[rivi][sarake] = (rivi+1)*(sarake+1)

    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(matriisi)
    print()
    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    for rivi in range(rivit):
        for sarake in range(sarak):
            print(matriisi[rivi][sarake], end=";")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()