import sys

class LUOKKA():
    nimi = ""
    maara = 0

def lue():
    lista = []
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "r", encoding="utf-8")
        tiedosto.readline()
        for rivi in tiedosto.readlines():
            rivi = rivi.split(";")
            lista.append(rivi)
        tiedosto.close()
    except Exception:
        print(f"Virhe tiedoston {tiedostonimi} käsittelyssä.")
        sys.exit(0)
    return lista

def analysoi(lista):
    uusilista = []
    for i in range(lista[0]):
        uusilista.append(lista[1][i])
    return uusilista

def tallenna(lista):
    tiedostonimi = input("Anna tallennettavan tiedoston nimi: ")
    try:
        tiedosto = open(tiedostonimi, "w", encoding="utf-8")
        tiedosto.write("Otsikkorivi")
        for rivi in lista:
            tiedosto.write(rivi+"\n")
        tiedosto.close()
    except Exception:
        print("Virhe tallettaessa")
        sys.exit(0)
    return None