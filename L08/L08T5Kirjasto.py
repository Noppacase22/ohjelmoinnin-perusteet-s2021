class TUOTE():
    nimi = ""
    arvo = 0.0
    maara = 0

def LueTiedosto(tiedostonimi):
    tiedosto = open(tiedostonimi, "r")
    lista = []
    for rivi in tiedosto.readlines():
        arvot = rivi.split(";")
        tavara = TUOTE()
        tavara.nimi = arvot[0]
        tavara.arvo = float(arvot[2])
        tavara.maara = int(arvot[1])
        lista.append(tavara)
    tiedosto.close()
    print(f"Tiedosto '{tiedostonimi}' luettu, {len(lista)} riviä.")
    return lista

def Varastoi(lista):
    varasto = 0
    for olio in lista:
        varasto += olio.arvo * olio.maara
    print("Tiedot analysoitu, varaston arvo on {0:.2f} EUR.".format(varasto))

def TalletaTiedosto(tiedostonimi, lista):
    tiedosto = open(tiedostonimi, "w")
    for olio in lista:
        arvo = olio.arvo * olio.maara
        tiedosto.write("{0:.2f}\n".format(arvo))
    print(f"Tulokset tallennettu tiedostoon '{tiedostonimi}'.")