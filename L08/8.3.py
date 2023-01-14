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

import datetime

def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while True:
        valikko()
        valinta = input("Valintasi: ")
        if valinta == "0":
            break
        elif valinta == "1":
            aika = datetime.datetime.strptime(input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': "), "%d.%m.%Y %H:%M")
            print(aika.strftime("Annoit vuoden %Y"))
            print(aika.strftime("Annoit kuukauden %m"))
            print(aika.strftime("Annoit päivän %d"))
            print(aika.strftime("Annoit tunnin %H"))
            print(aika.strftime("Annoit minuutin %M"))

        elif valinta == "2":
            syntymapaiva = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
            syntymapaiva = datetime.datetime.strptime(syntymapaiva, "%d.%m.%Y")
            paivat = 365*(2000-syntymapaiva.year) -int(syntymapaiva.strftime("%j")) +1
            if paivat<0:
                print("1.1.2000 sinä olit 0 päivää vanha.")
            else:
                print(f"1.1.2000 sinä olit {paivat} päivää vanha.")

        elif valinta == "3":
            paiva = datetime.datetime.strptime("01.11.2021", "%d.%m.%Y")
            i = 0
            for i in range(7):
                i+=1
                print(paiva.strftime("%A"))
                paiva = paiva + datetime.timedelta(days=1)

        elif valinta == "4":
            paiva = datetime.datetime.strptime("01.01.2021", "%d.%m.%Y")
            i = 0
            for i in range(12):
                i+=1
                print(paiva.strftime("%b"))
                paiva += datetime.timedelta(days=31)

        else:
            print("Tuntematon valinta.")
        print()
    print("Kiitos ohjelman käytöstä.")

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Tunnistaa aika-olion komponentit")
    print("2) Laskea iän päivinä")
    print("3) Tulostaa viikonpäivät")
    print("4) Tulostaa kuukaudet")
    print("0) Lopeta")

paaohjelma()