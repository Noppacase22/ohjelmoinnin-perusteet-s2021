def paaohjelma():
    tiedosto = input("Anna luettavan tiedoston nimi: ")
    LueTiedosto(tiedosto)
    print("Kiitos ohjelman käytöstä.")
    return

def LueTiedosto(tiedosto):
    tiedosto = open(tiedosto, "r", encoding="UTF-8")
    nimet = 0
    merkit = 0
    for nimi in tiedosto.readlines():
        if len(nimi) == 0:
            break
        else:
            nimet = nimet + 1
            merkit = merkit + len(nimi)
    print("Tiedostossa oli", nimet, "nimeä ja", merkit, "merkkiä.")
    print("Keskimääräinen nimen pituus oli", round((merkit-nimet)/nimet), "merkkiä.")
    return

paaohjelma()