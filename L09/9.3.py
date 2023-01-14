######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 11.11.2021
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
    uusilista = analysoi(lista)
    tallenna(tallettavanimi, uusilista)
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
    uusilista = []
    for rivi in lista:
        i = 0
        for auto in uusilista:
            if auto == rivi:
                i = 1
                continue
        if i == 0:
            uusilista.append(rivi)
    print(f"Tiedostossa oli {len(uusilista)} eri automerkkiä.")
    return uusilista

def tallenna(tiedostonimi, lista):
    try:
        tiedosto = open(tiedostonimi, "w")
        for auto in lista:
            print(auto)
            tiedosto.write(f"{auto}\n")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

paaohjelma()