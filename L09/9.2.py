######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 08.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def paaohjelma():
    while True:
        valinta = valikko()
        if valinta == 0:
            break
        elif valinta == 1:
            print("Valikko-ohjelma testaa ValueError'n.")
        elif valinta == 2:
            Indeksoija()
        elif valinta == 3:
            Jaa()
        elif valinta == 4:
            Tyyppi()
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
    print("Kiitos ohjelman käytöstä.")

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    print("0) Lopeta")
    while True:
        syote = input("Valintasi: ")
        try:
            valinta = int(syote)
            return valinta
        except ValueError:
            print("Anna valinta kokonaislukuna.")

def Indeksoija():
    lista = [11,22,33,44,55]
    indeksi = input("Anna indeksi 0-4: ")
    try:
        print(f"Listan arvo on {lista[int(indeksi)]} indeksillä {indeksi}.")
    except IndexError:
        print(f"Tuli IndexError, indeksi {indeksi}.")

def Jaa():
    luku = int(input("Anna jakaja: "))
    try:
        print(f"4/{luku} on  {(4/luku):.2f}.")
    except ZeroDivisionError:
        print(f"Tuli ZeroDivisionError, jakaja {luku}.")

def Tyyppi():
    luku = input("Anna numero: ")
    try:
        print(luku*luku)
    except TypeError:
        print(f"Tuli TypeError, {luku}*{luku} merkkijonoilla ei onnistunut.")

paaohjelma()