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
    tiedosto = input("Anna tiedoston nimi: ")
    lukija = open(tiedosto, "r")
    lukija.readline()
    for rivi in lukija.readlines():
        rivi = rivi.split(";")
        print(f"Kello oli {rivi[2][:-1]}, kun punnittiin marjoja {rivi[0]}.")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()