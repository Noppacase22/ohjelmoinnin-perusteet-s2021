# (c) LUT 2020 L11T4.py un
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
######################################################################
# Ohjelma, joka etsii sopivia numeroita

import time
import sys

def Hakufunktio():
    Luvut = ["",""]
    Luvut[0] = 0  #Pienempi luku tallennetaan tähän
    Luvut[1] = 0  #Suurempi luku tallennetaan tähän

# Lisättävä koodi alkaa alta.
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

    tiedostonimi = input("Anna tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "r")
        a = 0
        b = 0
        for rivi in tiedosto.readlines():
            luku = int(rivi[:-1])
            if a == 0:
                a = luku
            if luku > b:
                b = luku
            elif luku < a:
                a = luku
            if a*3 < b:
                Luvut[0] = a
                Luvut[1] = b
                return Luvut
        Luvut[0] = 0
        Luvut[1] = 0
        return Luvut
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)


# Lisättävä koodi loppuu ylle.  

def paaohjelma():
    Kello1 = time.perf_counter()
    Tulosluvut = Hakufunktio()
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    if ((Tulosluvut[0] == 0) and (Tulosluvut[1] == 0)):
        print("Hakualgoritmisi ei löytänyt sopivaa lukuparia.")
    elif (Aika > 2):
        print("Hakualgoritmisi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmisi oli riittävän nopea!")
        print("Se löysi sopivan parin:", Tulosluvut[0], "ja", Tulosluvut[1])
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

###########################################################################
# eof
