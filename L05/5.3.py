def tulosta(lause, luku):
    if luku == 0:
        return
    print(lause)
    tulosta(lause, luku-1)

jatka = True
while jatka:
    lause = input("Anna teksti: ")
    if lause == "lopeta":
        print("Lopetetaan.")
        break
    luku = int(input("Anna luku: "))
    tulosta(lause, luku)
    print()
print("Kiitos ohjelman käytöstä.")