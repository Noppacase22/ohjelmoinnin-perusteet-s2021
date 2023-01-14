######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 07.12.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import sys

def paaohjelma():
    print("Syötteen parilliset luvut ovat seuraavat:")
    rivi = ""
    aa = 0
    ka = 0
    for a in sys.argv:
        try: 
            if int(a)%2 == 0:
                rivi = rivi + a + " "
                aa += 1
                ka += int(a)
        except Exception:
            Exception
    if aa > 0:
        ka = ka/aa
    print(rivi)
    print("Lukujen keskiarvo on {0:.2f}.".format(ka))
    print("Kiitos ohjelman käytöstä.")

paaohjelma()