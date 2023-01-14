######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 29.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

from os import abort
import sys

def lue(tiedostonimi):
    try:
        tiedosto = open(tiedostonimi, "r", encoding="utf-8")
        lista = []
        tiedosto.readline()
        for rivi in tiedosto.readlines():
            lista.append(rivi[:-1])
        tiedosto.close()
        print(f"Tiedosto '{tiedostonimi}' luettu, {len(lista)+1} riviä.")
    except Exception:
        print(f"Tiedoston '{tiedostonimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista

def analysoi(lista):
    uusilista = []
    for i in range(len(lista)):
        rivi = lista[i]
        a = rivi.split(";")
        if len(a) != 3:
            print(f"Väärä määrä arvoja, rivi {i+2}: '{rivi}'")
            continue
        else:
            try:
                b = a[0]
                luku = int(b)
                if len(b) !=4 or luku < 0:
                    print(f"Virheellinen ID, rivi {i+2}: '{rivi}'")
                    continue
            except Exception:
                print(f"Virheellinen ID, rivi {i+2}: '{rivi}'")
                continue
        jono = a[1]
        uusijono = ""
        for i in range(len(jono)):
            char = jono[i]
            if char.isalnum():
                uusijono = uusijono + char
        maine = a[2]
        try:
            c = int(maine)
        except Exception:
            c = 0
        uusilista.append(f"{a[0]};{uusijono};{c}")
    print(f"Tiedot analysoitu, {len(uusilista)} hyväksyttävää tietoalkiota.")
    return uusilista

def tallenna(lista):
    try:
        tiedosto = open("siistitty.txt", "w", encoding="utf-8")
        a = "ID;Kommentti;Mainepisteet\n"
        tiedosto.write(a)
        for rivi in lista:
            tiedosto.write(f"{rivi}\n")
        print(f"Tiedosto 'siistitty.txt' kirjoitettu, {len(lista)+1} riviä.")
    except Exception:
        print("Virhe.")
        sys.exit(0)
    return None

def paaohjelma():
    lista = []
    uusilista = []
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    lista = lue(tiedostonimi)
    uusilista = analysoi(lista)
    tallenna(uusilista)
    lista.clear()
    uusilista.clear()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()