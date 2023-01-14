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

def juuri(luku):
    for i in range(luku):
        if i*i>= luku:
            if i*i-luku > luku-i*i+2*i-1:
                return i-1
            else:
                return i

def paaohjelma():
    luku = int(input("Anna luku: "))
    nelio = juuri(luku)
    print(f"Neliöjuuri on {nelio}")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()