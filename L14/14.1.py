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

import math

def main():
    km = int(input("Anna vuotuiset kilometrit: "))
    kulutus = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
    hinta = float(input("Anna polttoaineen hinta (€/l): "))
    ika = int(input("Anna auton ikä vuosissa: "))
    vakuutus = int(input("Anna vakuutusten määrä (euroissa): "))
    bonus = int(input("Anna bonusprosentti kokonaislukuna: "))
    verot = int(input("Anna verojen määrä: "))
    s = 0
    for i in range(5):
        raha = km/100*kulutus*hinta + vakuutus*(100-bonus)/100 + verot + 200 * math.sqrt(ika+i)
        print(f"{i+1}. vuosi: {round(raha)}")
        s += raha
    print(f"Viiden vuoden aikana autoon käytettiin rahaa {s} euroa.")
    print("Kiitos ohjelman käytöstä.")
    return None

main()