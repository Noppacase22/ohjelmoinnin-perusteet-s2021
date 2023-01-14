######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 24.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def rekursio(sana, luku):
    if luku == 0:
        return None
    rekursio(sana, luku-1)
    print(f"Sana on '{sana}', {luku}. kerta.")
    return None

def paaohjelma():
    sana = input("Anna tulostettava sana: ")
    luku = int(input("Anna tulostuskertojen määrä: "))
    rekursio(sana, luku)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()