def paaohjelma():
    tiedosto = input("Anna tallennettavan tiedoston nimi: ")
    TiedostoKirjoita(tiedosto)
    TiedostoLue(tiedosto)
    print("Kiitos ohjelman käytöstä.")
    return

def TiedostoKirjoita(tiedosto):
    tiedosto = open(tiedosto, "w")
    tiedosto.flush
    while True:
        nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
        if nimi == "0":
            tiedosto.close()
            break
        else:
            tiedosto.write(nimi + "\n")
    return

def TiedostoLue(tieto):
    tiedosto = open(tieto, "r")
    print("Tiedostoon '" + tieto + "' on tallennettu seuraavat nimet:")
    for nimi in tiedosto.readlines():
        if len(nimi) == 0:
            break
        print(nimi, end = "")
    return

paaohjelma()