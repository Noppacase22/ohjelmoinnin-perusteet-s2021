######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 29.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def muunna(luku):
    a = 0
    for i in range(len(luku)):
        a += int(luku[i])*2**(len(luku)-i-1)
    print(f"Bittijonosi {luku} on kymmenkantaisena kokonaislukuna {a}")
    return a

def paaohjelma():
    luku1 = input("Anna ensimmäinen binaariluku: ")
    luku2 = input("Anna toinen binaariluku: ")
    luku1 = muunna(luku1)
    luku2 = muunna(luku2)
    summa = luku1-luku2
    print(f"Lukujen {luku1} ja {luku2} erotus on {summa}")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()