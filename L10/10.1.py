######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 15.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import sys

def paaohjelma():
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    tallettavanimi = input("Anna kirjoitettavan tiedoston nimi: ")
    lista = lue(tiedostonimi)
    kirja = analysoi(lista)
    tallenna(tallettavanimi, kirja, lista)
    print("Kiitos ohjelman käytöstä.")

def lue(tiedostonimi):
    lista = []
    try:
        tiedosto = open(tiedostonimi, "r")
        for rivi in tiedosto.readlines():
            lista.append(rivi.strip())
        if len(lista) == 0:
            print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
            print("Kiitos ohjelman käytöstä.")
            sys.exit(0)
        else:
            return lista
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def analysoi(lista):
    kirjasto = {}
    for rivi in lista:
        try:
            kirjasto.update({rivi : kirjasto.get(rivi)+1})
        except Exception:
            kirjasto.update({rivi : 1})
    return kirjasto

def tallenna(tiedostonimi, kirjasto, lista):
    try:
        tiedosto = open(tiedostonimi, "w")
        autot = f"Tunnistettiin {len(kirjasto)} automerkkiä ja {len(lista)} autoa:"
        print(autot)
        tiedosto.write(f"{autot}\n")
        for avain in kirjasto:
            if kirjasto.get(avain) == 1:
                stringi = f"{avain}: 1 auto"
            else:
                stringi = f"{avain}: {kirjasto.get(avain)} autoa"
            print(stringi)
            tiedosto.write(f"{stringi}\n")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

paaohjelma()