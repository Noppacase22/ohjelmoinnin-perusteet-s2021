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

class AUTO():
    merkki = ""
    lukumaara = 0

def paaohjelma():
    auto = AUTO()
    auto.merkki = input("Anna automerkki: ")
    auto.lukumaara = input("Anna automerkin lukumäärä varastossa: ")
    tulosta_auto(auto)
    print("Kiitos ohjelman käytöstä.")

def tulosta_auto(auto):
    print(f"Varastossa on nyt {auto.merkki}-merkkisiä autoja {auto.lukumaara} kpl.")
paaohjelma()