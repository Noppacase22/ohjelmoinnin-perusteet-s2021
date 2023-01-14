######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 01.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import L08T2Kirjasto

def paaohjelma():
    print(f"Käytetään lämpötilamuunnoskirjaston versiota {L08T2Kirjasto.versio}")
    while True:
        valikko()
        valinta = input("Valintasi: ")
        if valinta == "0":
            break
        elif valinta == "1":
            tila = input("Anna lähtölämpötila: ")
            print(f"Lämpötila Fahrenheit asteina: {L08T2Kirjasto.CF(tila)}")
        elif valinta == "2":
            tila = input("Anna lähtölämpötila: ")
            print(f"Lämpötila Kelvin asteina: {L08T2Kirjasto.CK(tila)}")
        elif valinta == "3":
            tila = input("Anna lähtölämpötila: ")
            print(f"Lämpötila Kelvin asteina: {L08T2Kirjasto.FK(tila)}")
        elif valinta == "4":
            tila = input("Anna lähtölämpötila: ")
            print(f"Lämpötila Celsius asteina: {L08T2Kirjasto.FC(tila)}")
        elif valinta == "5":
            tila = input("Anna lähtölämpötila: ")
            print(f"Lämpötila Celsius asteina: {L08T2Kirjasto.KC(tila)}")
        elif valinta == "6":
            tila = input("Anna lähtölämpötila: ")
            print(f"Lämpötila Fahrenheit asteina: {L08T2Kirjasto.KF(tila)}")
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print()
    print("Kiitos ohjelman käytöstä.")

def valikko():
    print("Minkä lämpötilamuunnoksen haluat tehdä?")
    print("1) Celsius->Fahrenheit")
    print("2) Celsius->Kelvin")
    print("3) Fahrenheit->Kelvin")
    print("4) Fahrenheit->Celsius")
    print("5) Kelvin->Celsius")
    print("6) Kelvin->Fahrenheit")
    print("0) Lopeta")

paaohjelma()