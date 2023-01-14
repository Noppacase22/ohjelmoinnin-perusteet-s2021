######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 19.12.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import random
import sys

def tee(luvut):
    luvut = luvut.split(" ")
    i = int(luvut[0])
    mini = int(luvut[1])
    maks = int(luvut[2])

    if i > maks-mini+1:
        print("Arvottavia lukuja ei voi olla enemmän kuin erilaisia lukuja on.")
        print("Kiitos ohjelman käytöstä.")
        sys.exit(0)
    
    lista = []
    lista.append(f"Arvottu {i} lukua väliltä {mini}-{maks}:")

    while len(lista) < i+1:
        luku = random.randint(mini,maks)

        if luku not in lista:
            lista.append(luku)
    
    return lista

def kirjoita(apu):
    tiedostonimi = apu[0]
    lista = apu[1]

    try:
        tiedosto = open(tiedostonimi, "w", encoding="utf-8")
        for a in lista:
            tiedosto.write(f"{a}\n")
        tiedosto.close()
        print(f"Tiedosto '{tiedostonimi}' luotu, kiitos ohjelman käytöstä.")

    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    return None

def main():
    random.seed(1)

    print("Tämä ohjelma arpoo haluamasi määrän kokonaislukuja halutulta väliltä\nja kirjoittaa ne tekstitiedostoon.")

    tiedostonimi = input("Anna tehtävän tiedoston nimi: ")
    luvut = input("Anna lukujen määrä, alaraja ja yläraja, esim. 7 1 37: ")

    lista = tee(luvut)
    apu = [tiedostonimi, lista]
    kirjoita(apu)

main()