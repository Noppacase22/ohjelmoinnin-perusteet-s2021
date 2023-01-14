def vertaa(luku, toinen):
    if toinen > luku:
        print("Testatuista luvuista", toinen, "on suurempi kuin", luku)
        return toinen
    if luku > toinen:
        print("Testatuista luvuista", luku, "on suurempi kuin", toinen)
    else:
        print("Luvut ovat samansuuruiset.")
    return luku

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
voittaja = vertaa(luku1, luku2)
if voittaja == luku1:
    toinen = luku2
else:
    toinen = luku1
vertaa(voittaja - int(input("Paljonko vähennetään suuremmasta luvusta: ")), toinen)
print("Kiitos ohjelman käytöstä.")