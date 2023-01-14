def paaohjelma():
    tie = input("Anna luettavan tiedoston nimi: ")
    palindromi(tie)
    print("Kiitos ohjelman käytöstä.")
    return

def palindromi(tiedosto):
    lukeva = open(tiedosto, "r")
    talleta = open("L06T3T1.txt", "w")
    talleta.flush
    for rivi in lukeva.readlines():
        if len(rivi) == 0:
            return
        else:
            rivi = rivi[:-1]
        if rivi.isdigit():
            print("Rivi '" + rivi + "' on numerorivi.")
        elif rivi == rivi[::-1]:
            print("Rivi '" + rivi + "' on palindromi.")
            talleta.write(rivi + "\n")
        else:
            print("Rivi '" + rivi + "' ei ole palindromi.")
            
paaohjelma()