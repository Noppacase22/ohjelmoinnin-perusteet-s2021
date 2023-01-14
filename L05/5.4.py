def paa_ohjelma():
    kysy_merkkijono()
    print("Kiitos ohjelman käytöstä.")

def kysy_merkkijono():
    pituus = testaa_merkkijono(input("Anna merkkijono, 5-15 merkkiä: "))
    if pituus < 5:
        print("Liian lyhyt,", pituus, "merkkiä, anna uusi.")
        kysy_merkkijono()
    elif pituus < 16:
        print("Annoit sopivan merkkijonon,", pituus, "merkkiä.")
    else:
        print("Liian pitkä,", pituus, "merkkiä, anna uusi.")
        kysy_merkkijono()

def testaa_merkkijono(jono):
    i = 0
    for merkki in jono:
        i = i + 1
    return i

paa_ohjelma()