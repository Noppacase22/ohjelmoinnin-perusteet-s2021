######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 18.10.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def paaohjelma():
    lista = []
    while True:
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        print(lista)
        print("Voit valita alla olevista toiminnoista:\n1) Lisää\n2) Poista\n0) Lopeta")
        valinta = input("Valintasi: ")
        if valinta == "1":
            lista.append(input("Anna lisättävä tuote: "))
        elif valinta == "2":
            print("Ostoslistassasi on {0} tuotetta.".format(len(lista)))
            lista.remove(lista[int(input("Anna poistettavan tuotteen järjestysnumero: "))-1])
        elif valinta == "0":
            print("Sinulta jäi ostamatta seuraavat tuotteet:")
            print(lista)
            break
        else:
            print("Tunnistamaton valinta.")
        print()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()