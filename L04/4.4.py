ala = int(input("Anna alueen alaraja: "))
yla = int(input("Anna alueen yläraja: "))
while ala <= yla and ala % 35 != 0:
    if ala % 5 > 0:
        print(ala, "ei ole jaollinen viidellä, hylätään.")
    else:
        print(ala, "ei ole jaollinen seitsemällä, hylätään.")
    ala = ala + 1
if ala > yla:
    print("Alueelta ei löytynyt sopivaa arvoa.")
else:
    print("Luku", ala, "on jaollinen 5:llä ja 7:llä.")
    print("Lopetetaan etsintä.")
print("Kiitos ohjelman käytöstä.")