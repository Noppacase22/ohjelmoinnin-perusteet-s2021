def vaihe1():
    print("Ensimmäinen vaihe:")
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Tämä sopii hyvin valikon tulostamiseen.")
    print()
    return

def vaihe2(luku):
    print("Aliohjelmassa parametrin arvo on", luku)
    luku = luku**2
    print("Aliohjelmassa parametrin arvo on neliöön korottamisen jälkeen", luku)
    return

def vaihe3(nimi, suku):
    print("Etunimi '" + nimi + "' ja sukunimi '" + suku + "' muodostavat nimen '" + nimi, suku + "'.")
    return

vaihe1()

print("Toinen vaihe:")
luku = int(input("Anna luku: "))
print("Päätasolla ennen aliohjelmaa luku on", luku)
vaihe2(luku)
print("Päätasolla aliohjelman jälkeen luku on", luku)
print()

print("Kolmas vaihe:")
nimi = input("Anna etunimi: ")
suku = input("Anna sukunimi: ")
vaihe3(nimi, suku)
print("Kiitos ohjelman käytöstä.")