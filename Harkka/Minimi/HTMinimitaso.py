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
    # Analyysin toteutus luomalla viikko*viikkotehtävät lista, johon kirjataan jokainen tehty tehtävä.
    # Rakenne muistuttaa kirjastoa, jossa avaimen sijasta käytetään indeksiä, joka saadaan
    # kaavalla 5*viikko + tehtävänumero -1 -5, -1 koska ensimmäinen tehtävän tulee olla kohdassa 0,
    # ja -5 samasta syystä viikkoja varten (ensimmäinen viikko on nyt 0-4, ei 5-9).
    # Nyt tosin on kovakoodattu tehtävien määrä etukäteen. Jos ei tiedetä, montako tehtävää on,
    # pitää lisätä analyysialiohjelma joka lukee viimeisen palautuksen arvon ja määrittää koon sen mukaan.

    # Toinen tapa, jonka keksin vasta viimeistelyvaiheessa, on pitää listaa, jossa on alkioina
    # tehtävän numero, jota seuraa kyseisen tehtävän lukumäärä aineistossa, ja sitten seuraava jne. Listaa käydääm läpi
    # jäsenfunktioilla count(), joilla ensin tarkastetaan onko tehtävä listassa. Jos ei ole, lisätään.
    # Jos on, etsitään paikka index() jäsenfunktiolla ja muokataan sitä seuraavaa alkiota lisäämällä siihen +1.
    # Koska uuden listan rakenne tiedetään etukäteen, on sen läpikäynti helppoa.
    # Tällä menetelmällä laajentamisongelmaa ei ole.

    tuloslista = []
    for i in range(70):             # Luodaan tyhjä 70(=14*5) paikan lista tiedon lajittelua varten
        tuloslista.append(0)
    
    tehtavamaara = 0
    eniten = 0
    for rivi in lista:
        viikko = rivi[1:3] 
        tehtava = rivi[-1]
        indeksi = 5*int(viikko) + int(tehtava)-6        # Lasketaan tehtävälle indeksiarvo
        tuloslista[indeksi] += 1                            # Lisätään luettu tehtävä listaan omalle paikalleen
        if tuloslista[indeksi]==1:                          ## Katsotaan onko tehtävä ensimmäinen lajiaan
            tehtavamaara += 1                               ## Jos on, lisätään se laskuriin
        if tuloslista[indeksi] > tuloslista[eniten]:    # Tarkistetaan, onko kyseistä tehtävää eniten
            eniten = indeksi                            ## Jos on, merkitään sen indeksi muistiin

    vahiten = 0
    for i in range(70):
        if tuloslista[i] > 0:
            if tuloslista[i] < tuloslista[vahiten]:
                vahiten = i

    kokonaismaara = len(lista)
    keskimaara = int(kokonaismaara/tehtavamaara)
    print(f"Analysoitu {kokonaismaara} palautusta {tehtavamaara} eri tehtävään.")

    palautus = f"Palautuksia tuli yhteensä {kokonaismaara}, {tehtavamaara} eri tehtävään."
    palautukset = f"Viikkotehtäviin tuli keskimäärin {keskimaara} palautusta."
    suurin = f"Eniten palautuksia, {tuloslista[eniten]}, tuli viikkotehtävään {tehtavanumero(eniten)}."
    pienin = f"Vähiten palautuksia, {tuloslista[vahiten]}, tuli viikkotehtävään {tehtavanumero(vahiten)}."

    talletuslista = []
    talletuslista.append(palautus)
    talletuslista.append(palautukset)
    talletuslista.append(suurin)
    talletuslista.append(pienin)
    talletuslista.append("")
    talletuslista.append("Tehtävä;Lukumäärä")

    for i in range(70):
        if tuloslista[i] > 0:
            kirjoitus = f"{tehtavanumero(i)};{tuloslista[i]}"
            talletuslista.append(kirjoitus)
    
    return talletuslista

def tehtavanumero(luku):
    luku = int(luku)
    viikkoluku = int(luku/5)+1
    tehtavaluku = 5 * (luku/5-viikkoluku)+6
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
    tuloslista = []
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
                tuloslista = analysoi(lista)
                print("Tilastotiedot analysoitu.")
        elif valinta == "3":
            if tuloslista == []:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                tallenna(tuloslista)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        print("Anna uusi valinta.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()