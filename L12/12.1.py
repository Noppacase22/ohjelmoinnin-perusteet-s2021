######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 29.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def testaa(hlo):
    sarja = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    tarkistusluku = hlo[-1]
    luku = int(hlo[0:6]+hlo[-4:-1])
    uusi = luku/31
    jaannos = int(round(31*(uusi-int(uusi)),1))
    if sarja[jaannos] == tarkistusluku.upper():
        print("Henkilötunnus hyväksytty.")
    else:
        print("Henkilötunnusta ei hyväksytä.")
    return None

def paaohjelma():
    hlo = input("Anna henkilötunnus: ")
    if hlo[0:6].isdigit() and hlo[-4:-1].isdigit():
        testaa(hlo)
    else:
        print("Henkilötunnusta ei hyväksytä.")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()