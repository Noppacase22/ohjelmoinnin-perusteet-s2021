def kirjaa(tiedosto,tuloslista):
    tallenna = open(tiedosto, "w")
    for rivi in tuloslista:
        tallenna.write(rivi)
    print(f"Tallennettu tiedosto '{tiedosto}'.")
    tuloslista.clear()

def LueLuku(luvut):
    tiedosto = open(luvut, "r")

    lista = []
    for rivi in tiedosto.readlines():
        luku = rivi[:-1]
        lista.append(luku)
    lista.reverse()
    print(f"Luettu tiedosto '{luvut}'.")
    return lista

def Summa(luku1, luku2):
    summa = int(luku1)+int(luku2)
    print("Tulos lisätty listaan.")
    return ("Summa {0} + {1} = {2}\n".format(luku1, luku2, summa))

def Osamaara(luku1, luku2):
    if luku2 != 0:
        print("Tulos lisätty listaan.")
        return ("Osamäärä {0} / {1} = {2}\n".format(luku1, luku2, round(int(luku1)/int(luku2),2)))
    else:
        print("Nollalla ei voi jakaa.")