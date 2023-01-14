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

def kanit(luku):
    i = 1
    j = 0
    for a in range(luku):
        b = j
        j = i
        i += b
    return i

def paaohjelma():
    kk = int(input("Anna kuukausien lukumäärä: "))
    lkm = kanit(kk)
    print(f"Kanipariskuntia on {kk} kuukauden kuluttua {lkm}")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()