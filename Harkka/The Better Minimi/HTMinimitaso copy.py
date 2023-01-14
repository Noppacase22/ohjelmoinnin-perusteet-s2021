######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 20.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import sys

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    valinta = input("Valintasi: ")
    return valinta

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
    tuloslista = []
    tehtavamaara = 0
    for rivi in lista:
        viikko = int(rivi[1:3])
        tehtava = int(rivi[5:])
        while viikko > len(tuloslista):
            tuloslista.append([])
        while tehtava > len(tuloslista[viikko-1]):
            tuloslista[viikko-1].append(0)
            tehtavamaara += 1
        tuloslista[viikko-1][tehtava-1] += 1

    vahiten = [0, 0]
    eniten = [0, 0]
    for i in range(len(tuloslista)):
        for j in range(len(tuloslista[i])):
            if tuloslista[i][j] < tuloslista[vahiten[0]][vahiten[1]]:
                vahiten = [i, j]
            if tuloslista[i][j] > tuloslista[eniten[0]][eniten[1]]:
                eniten = [i, j]

    kokonaismaara = len(lista)
    keskimaara = int(kokonaismaara/tehtavamaara)
    print(f"Analysoitu {kokonaismaara} palautusta {tehtavamaara} eri tehtävään.")

    palautus = f"Palautuksia tuli yhteensä {kokonaismaara}, {tehtavamaara} eri tehtävään."
    palautukset = f"Viikkotehtäviin tuli keskimäärin {keskimaara} palautusta."
    suurin = f"Eniten palautuksia, {tuloslista[eniten[0]][eniten[1]]}, tuli viikkotehtävään {tehtavanumero(eniten)}."
    pienin = f"Vähiten palautuksia, {tuloslista[vahiten[0]][vahiten[1]]}, tuli viikkotehtävään {tehtavanumero(vahiten)}."

    talletuslista = []
    talletuslista.append(palautus)
    talletuslista.append(palautukset)
    talletuslista.append(suurin)
    talletuslista.append(pienin)
    talletuslista.append("")
    talletuslista.append("Tehtävä;Lukumäärä")

    for i in range(len(tuloslista)):
        for j in range(len(tuloslista[i])):
            if tuloslista[i][j] > 0:
                kirjoitus = f"{tehtavanumero([i, j])};{tuloslista[i][j]}"
                talletuslista.append(kirjoitus)
    tuloslista.clear()
    return talletuslista

def tehtavanumero(indeksit):
    viikkoluku = indeksit[0]+1
    tehtavaluku = indeksit[1]+1
    if viikkoluku < 10:
        viikkoluku = f"0{viikkoluku}"
    tehtava = "L{0}-T{1:.0f}".format(viikkoluku,tehtavaluku)
    return tehtava

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

def paaohjelma():
    lista = []
    talletuslista = []
    while True:
        valinta = valikko()
        if valinta == "0":
            break
        elif valinta == "1":
            lista = lue()
        elif valinta == "2":
            if lista == []:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                talletuslista = analysoi(lista)
                print("Tilastotiedot analysoitu.")
        elif valinta == "3":
            if talletuslista == []:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                tallenna(talletuslista)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        print("Anna uusi valinta.")
    print("Kiitos ohjelman käytöstä.")
    lista.clear()
    talletuslista.clear()
    return None

paaohjelma()