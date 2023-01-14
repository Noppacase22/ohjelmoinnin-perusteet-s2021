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

import L09T4Kirjasto

def paaohjelma():
    luvut = input("Anna luettavan tiedoston nimi: ")
    kirjoita = input("Anna kirjoitettavan tiedoston nimi: ")
    luettu = 0
    tuloslista = []
    while True:
        toiminto = valikko(luvut)
        if toiminto == "1":            
            if luettu == 0:
                lista = L09T4Kirjasto.LueLuku(luvut)
                luettu = 1
            if lista == []:
                print("Luvut loppuivat, lopeta ohjelma.")
            else:
                luku1 = lista.pop()
                luku2 = lista.pop()
                print(f"Luettiin luvut {luku1} ja {luku2}")
        elif toiminto == "2":
            tuloslista.append(L09T4Kirjasto.Summa(luku1,luku2))
        elif toiminto == "3":
            tuloslista.append(L09T4Kirjasto.Osamaara(luku1, luku2))
        elif toiminto == "0":
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    if len(tuloslista) == 0:
        print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.")
    else:
        L09T4Kirjasto.kirjaa(kirjoita,tuloslista)
        tuloslista.clear()
    print("Kiitos ohjelman käytöstä.")
    return

def valikko(luvut):
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    return input("Valitse toiminto (0-3): ")

paaohjelma()