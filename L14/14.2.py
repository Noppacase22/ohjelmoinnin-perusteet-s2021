######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Elias Ryökäs
# Opiskelijanumero: 463223
# Päivämäärä: 19.12.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import sys

def main():
    lista = []
    tnimi = input("Anna luettavan tiedoston nimi: ")

    a = 0
    try:
        tiedosto = open(tnimi, "r", encoding="utf-8")
        for rivi in tiedosto.readlines():
            i = True
            a += 1
            rivi = rivi[:-1]
            for kirjain in rivi:
                if kirjain.isnumeric():
                    i = False
                    break
            if i == True:
                lista.append(rivi.lower())
    except Exception:
        print(f"Tiedoston '{tnimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    print(f"Luettiin {a} riviä tiedostosta '{tnimi}'.")
    print(f"Hylättiin {a-len(lista)} riviä.")

    tnimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        tiedosto = open(tnimi, "w", encoding="utf-8")
        for i in lista:
            tiedosto.write(f"{i}\n")
        tiedosto.close()
    except Exception:
        print(f"Tiedoston '{tnimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print(f"Kirjoitettiin {len(lista)} riviä tiedostoon '{tnimi}'.")
    print("Kiitos ohjelman käytöstä.")
    return None

main()