import Film


def beolvas():
    lista = []
    beFajl = open("film.txt", "r", encoding="utf-8")
    beFajl.readline()
    sorok = beFajl.readlines()
    beFajl.close()
    for index in range(len(sorok)):
        tisztitottSor = sorok[index].strip()
        daraboltSor = tisztitottSor.split(";")
        filmeim = Film.Film(daraboltSor[0],daraboltSor[1],daraboltSor[2], daraboltSor[3], daraboltSor[4])
        lista.append(filmeim)
    return lista
def kiir(lista):
    for index in range(len(lista)):
        print(lista[index])

def miniumKereses(lista):
    index = 0
    legkisebb = 0
    while index<len(lista):
        if lista[index].perc < lista[legkisebb].perc:
            legkisebb = index
        index += 1
    print(f"A legrövidebb film {lista[legkisebb].cim}")

def szamlalas(lista):
    kiFajl = open("110perces.txt", "w", encoding="utf-8")
    db = 0
    for index in range(len(lista)):
        if int(lista[index].perc) >= 110:
            db += 1
    print(f"{db} darab legalább 110 perces film van!")
    kiFajl.write(f"{db} darab legalább 110 perces film van!")
    kiFajl.close()

def szineszek(lista):
    szinesz = input("Adja meg a színész nevét:")
    vanE = False
    for index in range(len(lista)):
        if szinesz == lista[index].foszereplo:
            vanE = True
            print(f"{lista[index].cim}")
    if vanE == False:
        print("Nincs találat!")
