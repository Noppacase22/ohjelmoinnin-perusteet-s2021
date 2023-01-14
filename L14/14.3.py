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

import datetime

def main():
    vuosi = int(input("Anna vuosi: "))
    kk = int(input("Anna kuukausi: "))
    try:
        paiva = datetime.date(vuosi,kk,1)
        vertailu = datetime.date(vuosi,kk+1,1)
        maks = (vertailu - paiva).days
    except Exception:
        maks = 31
    uusi = paiva.weekday()
    print("Kalenteri näyttää seuraavalle:")
    print(" Ma Ti Ke To Pe La Su")
    string = ""
    aa = 1
    for a in range(7):
        if a < uusi:
            string += "   "
        else:
            string += f"  {aa}"
            aa += 1
    print(string)
    string = ""
    while aa <= maks:
        if aa < 10:
            string = f"{string}  {aa}"
        else:
            string = f"{string} {aa}"
        if (aa+uusi) % 7 == 0:
            print(string)
            string = ""
        elif aa == maks:
            print(string)
        aa += 1

main()