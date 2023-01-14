## juuh

import Kirjasto

def valikko():
    print("Valinta 1")
    print("Valinta 2")
    print("Valinta 3")
    print("Valinta 4")
    print("Valinta 0 Lopeta")
    valinta = input("Valintasi: ")
    return valinta

def paaohjelma():
    lista = []
    uusilista = []
    print("Tämä ohjelma...")
    while True:
        valinta = valikko()
        if valinta == "1":
            lista = Kirjasto.lue()
        if valinta == "2":
            if len(lista)>0:
                uusilista = Kirjasto.analysoi(lista)
            else:
                print("Lue ensin")
        if valinta == "3":
            if len(uusilista) > 0:
                Kirjasto.tallenna(uusilista)
            else:
                print("Analysoi ensin)")
        if valinta == "0":
            break
    print("Kiitos...")
    lista.clear()
    uusilista.clear()
    return None

paaohjelma()