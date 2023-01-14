######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 21.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import sys

class TEHTAVA():
    nimi = ""
    maara = 0

def lue():
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "r")
        lista = []
        tiedosto.readline()
        for rivi in tiedosto.readlines():
            rivi = rivi.split(";")
            lista.append(rivi[2][:-1])
        print(f"Tiedostosta '{tiedostonimi}' luettiin listaan {len(lista)} datarivin tiedot.")
        tiedosto.close()
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista

def analysoi(lista):
    tehtavalista = []
    oliolista = []
    for rivi in lista:
        if tehtavalista.count(rivi) == 0:
            tehtava = TEHTAVA()
            tehtava.nimi = rivi
            tehtava.maara = 1
            oliolista.append(tehtava)
            tehtavalista.append(rivi)
        else:
            olio = oliolista.pop()      # Käytetään hyväksi tietoa, että kaikki saman tyypin tehtävät ovat peräkkäin
            olio.maara += 1
            oliolista.append(olio)

    vahiten = oliolista[0]
    eniten = oliolista[0]
    for olio in oliolista:
        if olio.maara < vahiten.maara:
            vahiten = olio
        if olio.maara > eniten.maara:
            eniten = olio
    kokonaismaara = len(lista)
    tehtavamaara = len(tehtavalista)
    keskimaara = int(kokonaismaara/tehtavamaara)
    print(f"Analysoitu {kokonaismaara} palautusta {tehtavamaara} eri tehtävään.")

    palautus = f"Palautuksia tuli yhteensä {kokonaismaara}, {tehtavamaara} eri tehtävään."
    palautukset = f"Viikkotehtäviin tuli keskimäärin {keskimaara} palautusta."
    suurin = f"Eniten palautuksia, {eniten.maara}, tuli viikkotehtävään {eniten.nimi}."
    pienin = f"Vähiten palautuksia, {vahiten.maara}, tuli viikkotehtävään {vahiten.nimi}."

    talletuslista = []
    talletuslista.append(palautus)
    talletuslista.append(palautukset)
    talletuslista.append(suurin)
    talletuslista.append(pienin)
    talletuslista.append("")
    talletuslista.append("Tehtävä;Lukumäärä")

    for olio in oliolista:
        kirjoitus = f"{olio.nimi};{olio.maara}"
        talletuslista.append(kirjoitus)
    
    return talletuslista

def tallenna(lista):
    tiedostonimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "w", encoding="utf-8")
        for rivi in lista:
            print(rivi)
            tiedosto.write(f"{rivi}\n")
        print(f"Tulokset tallennettu tiedostoon '{tiedostonimi}'.")
        tiedosto.close()
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None