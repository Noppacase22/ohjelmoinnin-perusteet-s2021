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

class HENKILO():
    nimi = ""
    ika = 0
    nro = 0

def valikko():
    print("1) Anna tiedoston nimi")
    print("2) Lue tiedosto")
    print("3) Tulosta tiedot")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    return valinta

def nimi():
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    return tiedostonimi

def lue(tiedostonimi):
    try:
        tiedosto = open(tiedostonimi, "r", encoding="utf-8")
        lista = []
        for rivi in tiedosto.readlines():
            rivi = rivi.split(";")
            henkilo = HENKILO()
            henkilo.nimi = rivi[0]
            henkilo.nro = rivi[1]
            henkilo.ika = rivi[2][-1]
            lista.append(henkilo)
        tiedosto.close()
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista

def tulosta(lista):
    for henkilo in lista:
        print(f"{henkilo.nimi} on {henkilo.ika} vuotta vanha ja hänen puhelinnumero on {henkilo.nro}.")
    return None

def kirjoita(lista):
    ika = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): "))
    uusilista = []
    for henkilo in lista:
        if henkilo.ika >= ika:
            uusilista.append(henkilo)
    rivi = f"Tiedostossa on mukana {len(uusilista)} vähintään {ika} vuotiasta henkilöä:\n"
    try:
        tiedosto = open("tulos.txt", "w", encoding="utf-8")
        tiedosto.write(rivi)
        for a in uusilista:
            tiedosto.write(f"{a.nimi};{a.nro};{a.ika}\n")

    except Exception:
        print(f"Tiedoston 'tulos.txt' käsittelyssä virhe, lopetetaan.")

def paaohjelma():
    print("Tämä ohjelma lukee tiedoston ja tulostaa sen tiedot näytölle.")
    tiedot = []
    while True:
        valinta = valikko()
        if valinta == "0":
            break
        elif valinta == "1":
            tiedostonimi = nimi()
        elif valinta == "2":
            tiedot = lue(tiedostonimi)
        elif valinta == "3":
            tulosta(tiedot)
        elif valinta == "4":
            kirjoita(tiedot)
        else:
            print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()