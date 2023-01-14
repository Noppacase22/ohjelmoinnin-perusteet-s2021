def paaohjelma():
   # tiedosto = input("Anna tiedot sisältävän tiedoston nimi: ")
    tiedosto = "L06T4D1.txt"
    min = laskemin(tiedosto)
    max = laskemax(tiedosto)
    total = lasketotal(tiedosto)
    #toinen = input("Anna tallennettavan tiedoston nimi: ")
    toinen = "L06T4T1.txt"
    talleta(toinen, min, max, total)
    print("Kiitos ohjelman käytöstä.")
    return

def laskemin(tiedosto):
    minimi = -1
    tiedosto = open(tiedosto, "r")
    for rivi in tiedosto.readlines():
        luku = int(rivi[:-1])
        if minimi == -1:
            minimi = luku
        else:
            minimi = min(luku,minimi)
    return minimi

def laskemax(tiedosto):
    maksimi = -1
    tiedosto = open(tiedosto, "r")
    for rivi in tiedosto.readlines():
        luku = int(rivi[:-1])
        if maksimi == -1:
            maksimi = luku
        else:
            maksimi = max(luku,maksimi)
    return maksimi

def lasketotal(tiedosto):
    tiedosto = open(tiedosto, "r")
    total = 0
    for rivi in tiedosto.readlines():
        luku = int(rivi[:-1])
        total = total + luku
    return total

def talleta(tiedosto, min, max, total):
    tiedosto = open(tiedosto, "w", encoding="utf-8")
    rivimin = ("Pienin askelmäärä oli {0} askelta.".format(min))
    rivimax = ("Suurin askelmäärä oli {0} askelta.".format(max))
    rivitot = ("Yhteensä askelia oli {0} askelta.".format(total))
    tiedosto.write(rivimin + "\n")
    print(rivimin)
    tiedosto.write(rivimax + "\n")
    print(rivimax)
    tiedosto.write(rivitot + "\n")
    print(rivitot)
    return

paaohjelma()