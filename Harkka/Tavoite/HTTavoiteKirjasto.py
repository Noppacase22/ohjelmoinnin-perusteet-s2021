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
import datetime

class TEHTAVA():
    nimi = ""
    maara = 0

def lue():
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "r")  
        lista1 = []         # Palautusaika
        lista2 = []         # Opiskelijatunniste
        lista3 = []         # Tehtävänumero
        tiedosto.readline()     # Otsikkorivin poisto
        for rivi in tiedosto.readlines():   # Jaetaan rivi osiinsa ja talletetaan ne omiin listoihinsa
            rivi = rivi.split(";")          # Nyt aliohjelmat saavat vain tarvitsemansa tiedot helposti
            lista1.append(rivi[0])          # Kutsumalla vain tiettyjä alilistoja
            lista2.append(rivi[1])
            lista3.append(rivi[2][:-1])
        lista = [lista1, lista2, lista3]    # Palautetaan kaikki samalla listalla
        print(f"Tiedostosta '{tiedostonimi}' luettiin listaan {len(lista1)} datarivin tiedot.")
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
    lista.clear()
    return lista

def PisteAnalyysi(lista):
    opiskelijalista = {}
    for i in range(len(lista)):
        nimi = lista[i]
        try:                    # Kokeillaan, onko oppilas jo lisätty
            opiskelijalista.update({nimi : opiskelijalista.get(nimi)+1})
        except Exception:       # Jos ei ole, lisätään
            opiskelijalista.update({nimi : 1})

    tietolista = [0]
    for i in range(60):         # Alustetaan 60+1 paikkainen lista
        tietolista.append(0)
    for arvo in opiskelijalista.values():
        tietolista[arvo] += 1

    print("Tehtäväkohtaiset pisteet analysoitu.")
    tiedostonimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "w", encoding="utf-8")
        tiedosto.write("Pistemäärä;Opiskelijoita\n")
        for i in range(61):
            tiedosto.write(f"{i};{tietolista[i]}\n")
        tiedosto.close()
        print(f"Tulokset tallennettu tiedostoon '{tiedostonimi}'.")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    opiskelijalista.clear()
    tietolista.clear()
    return None

def TuntiAnalyysi(lista):
    Tuntimatriisi = luoMatriisi(14,24)
    for x in range(14):
        uusilista = []
        for y in range(24):
            uusilista.append(0)
        Tuntimatriisi.append(uusilista)
    
    aikalista = lista[0]
    tehtavalista = lista[2]
    for tehtava in range(len(aikalista)):   # Olisi varmaan ollut helpompaa ilman datetime-muunnosta, koska tiedetään tuntiarvon sijainti
        aika = datetime.datetime.strptime(aikalista[tehtava], "%d-%m-%Y %H:%M:%S")
        viikko = int(tehtavalista[tehtava][1:3])
        tunti = aika.strftime("%H")
        Tuntimatriisi[viikko-1][int(tunti)] = Tuntimatriisi[viikko-1][int(tunti)] +1
    print("Tuntikohtaiset palautukset analysoitu.")

    tiedostonimi = input("Anna kirjoitettavan tiedoston nimi: ")    
    merkkijono = "Tunti"    #Tehdään tiedoston otsikkorivi automaatiolla
    for i in range(24):
        merkkijono = f"{merkkijono};{i}"
    try:
        tiedosto = open(tiedostonimi, "w")
        tiedosto.write(merkkijono + "\n")
        viikko = 0
        tunti = 0
        for viikko in range(14):
            sana = f"Vko {viikko+1}"
            for tunti in range(24):
                sana = f"{sana};{Tuntimatriisi[viikko][tunti]}"
            tiedosto.write(f"{sana}\n")
        tiedosto.close()
        print(f"Tulokset tallennettu tiedostoon '{tiedostonimi}'.")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    Tuntimatriisi.clear()
    return None

def AikaAnalyysi(lista):    # Muistuttaa hyvin paljon edellisen kohdan tehtävää, otetaan siis mallia.
    Aikamatriisi = luoMatriisi(14,7) #Tehdään matriisi toiseen kertaan, joten siirretään sen koodi omaan aliohjelmaan.
    aikalista = lista[0]
    aloitusaika = datetime.datetime.strptime("01.09.2020 06:00:00", "%d.%m.%Y %H:%M:%S")

    for palautus in range(len(aikalista)):
        aika = datetime.datetime.strptime(aikalista[palautus], "%d-%m-%Y %H:%M:%S")
        viikkoaika = aika-aloitusaika       # Tein ensin ilman jakolaskua normalisoimalla aikamuuttujan listalla olevan tehtävän viikon mukaan. Nyt viikko saadaan suoraan datasta, ja päivä on viikkoaika.days muuttujan arvo.
        viikko = int(viikkoaika.days/7)     # Luin tehtävänannon uudelleen ja totesin kyseisen tavan olevan liian riskialtis sanoitukseen nähden, ja sen olisi voinut tuomita vääräksi.
        paiva = round(((viikkoaika.days/7)-viikko)*7, 1)
        if viikko == 6:             # Viikolla 7(indeksi 6) palautetut tehtävät ovat väleillä 0-3
            paiva = paiva/2
        if viikko == 7:             # Toisella viikolla palautetut tehtävät ovat väleillä 3-6
            paiva = paiva/2+3.5
        if viikko > 6:
            viikko += -1
        Aikamatriisi[viikko][int(paiva)] += 1
        
    print("Aikavälikohtaiset palautukset analysoitu.")

    tiedostonimi = input("Anna kirjoitettavan tiedoston nimi: ")    
    otsikko = "Aikaväli"
    for i in range(7):
        paivays = aloitusaika + datetime.timedelta(days=i)
        aikamaara = paivays.strftime("%a %H:%M")
        otsikko = f"{otsikko};{aikamaara}"
    try:
        tiedosto = open(tiedostonimi, "w", encoding="utf-8")
        tiedosto.write(otsikko + "\n")
        for viikko in range(14):
            sana = f"Vko {viikko+1}"
            for paiva in range(7):
                sana = f"{sana};{Aikamatriisi[viikko][paiva]}"
            tiedosto.write(sana + "\n")
        tiedosto.close()
        print(f"Tulokset tallennettu tiedostoon '{tiedostonimi}'.")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    Aikamatriisi.clear()
    return None

def luoMatriisi(rivit,sarakkeet):
    matriisi = []
    for x in range(rivit):
        lista = []
        for y in range(sarakkeet):
            lista.append(0)
        matriisi.append(lista)
    return matriisi