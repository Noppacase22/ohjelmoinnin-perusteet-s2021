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

import math
import random

def paaohjelma():
    random.seed(1)
    print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
    while True:
        valikko()
        valinta = input("Valintasi: ")
        if valinta == "1":
            ala()
        elif valinta == "2":
            arvaus()
        elif valinta == "0":
            break
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print()
    print("Kiitos ohjelman käytöstä.")

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Laskea ympyrän pinta-alan")
    print("2) Arvata luvun")
    print("0) Lopeta")

def ala():
    luku = int(input("Anna ympyrän säde kokonaislukuna: "))
    pa = round((math.pi * math.pow(luku, 2)), 2)
    print(f"Säteellä {luku} ympyrän pinta-ala on {pa}.")

def arvaus():
    print("Arvaa ohjelman arpoma kokonaisluku.")
    luku = random.randint(0,1000)
    laskuri = 0
    while True:
        laskuri += 1
        arvaus = int(input("Anna kokonaisluku välillä 0-1000: "))
        if arvaus == luku:
            print(f"Oikein! Käytit arvaamiseen {laskuri} kierrosta.")
            break
        elif arvaus < luku:
            print("Haettu luku on suurempi.")
        else:
            print("Haettu luku on pienempi.")

paaohjelma()