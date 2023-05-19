"""
0 - víz
1-9 - világító torony
11 - hajó
"""


feladvany_data = None
megoldas_data = None
darabolt_megoldas = None
tiltott_helyek = []
feladvany_path = r"C:\WORK\Peti_erettsegi\1. alkalom\3. feladat\data\feladvany.txt"
megoldas_path = r"C:\WORK\Peti_erettsegi\1. alkalom\3. feladat\data\megoldas.txt"

sor = 2
oszlop = 3
ertek = 3
rejtveny_terulet = None



def get_data_from_txt(file_path):
    with open(file_path, 'r') as f:
        data = f.read()

    return data

def feladat_1():
    """
    be kell kérni az input fv-el a sor, oszlop és ertek adatokat
    """
    global sor, oszlop, ertek

    sor = int(input("Sor: "))
    oszlop = int(input("Oszlop: "))
    ertek = int(input("Ertek: "))

    if ertek >= 3:
        print("Nehéz torony.")

def feladat_2_nem_jo():
    """
    a bekért számokhoz meg vissza kell adni, hogy mely pozíciókra nem tehetünk hajót
    a világító toronyhoz sem átlósan, sem közvetlen közelében nem lehet hajót lerakni
    sor: 2
    oszlop: 3

    mikor mozgathatjuk a sort
    mikor mozgathatjuk az oszlopot
    az irányát meg kell határozni

    """

    sor = 2
    oszlop = 3
    # megnézzük, hogy az első vagy utolsó sorbon vagy oszlopban van az érték
    # ez azért kell, mert akkor kevesebb pozíciót kell vizsgálni
    if sor in (1, 10) or oszlop in (1, 10):
        # maximum 5 db mezőt kell nzni

        # a sarkak beazonosítása
        if (sor == 1 and oszlop == 1) \
            or (sor == 1 and oszlop == 10) \
            or (sor == 10 and oszlop == 1) or (sor == 10 and oszlop == 10):
            # akkor a legkevesebb mezőt kell vizsgálni: 3 mezőt
            for item in rejtveny_terulet:
                print(item)

            print('---------------')

            aktualis_sor = sor - 1
            aktualis_oszlop = oszlop - 1
            tiltott_helyek = []

            if sor == 1 and oszlop == len(rejtveny_terulet[aktualis_sor]):
                # 1, 10

                tiltott_helyek.append(rejtveny_terulet[aktualis_sor][aktualis_oszlop -1])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor + 1][aktualis_oszlop -1])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor + 1][aktualis_oszlop])                
            
            if sor == 1 and oszlop == 1:
                # 1, 1
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor][aktualis_oszlop + 1])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor + 1][aktualis_oszlop])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor + 1][aktualis_oszlop + 1])
            

            if sor == len(rejtveny_terulet) and oszlop == 1:
                # 10, 1
                
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor][aktualis_oszlop + 1])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor - 1][aktualis_oszlop])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor - 1][aktualis_oszlop + 1])

            
            if sor == len(rejtveny_terulet) and oszlop == len(rejtveny_terulet[aktualis_sor]):
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor][aktualis_oszlop - 1])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor - 1][aktualis_oszlop])
                tiltott_helyek.append(rejtveny_terulet[aktualis_sor - 1][aktualis_oszlop - 1])

            print(tiltott_helyek)
        else:
            # itt 5 mezőt kell vizsgálni
           
            pass
    else:
        # sor = 6, oszlop = 6
        tiltott_helyek = []

        # az aktuális soromhoz tartozó lista adat
        aktualis_sor = sor - 1
        aktualis_oszlop = oszlop -1         

        # 
        tiltott_helyek.append(rejtveny_terulet[aktualis_sor-1][aktualis_oszlop-1])
        tiltott_helyek.append(rejtveny_terulet[aktualis_sor-1][aktualis_oszlop])
        tiltott_helyek.append(rejtveny_terulet[aktualis_sor-1][aktualis_oszlop+1])

        tiltott_helyek.append(rejtveny_terulet[aktualis_sor][aktualis_oszlop-1])
        tiltott_helyek.append(rejtveny_terulet[aktualis_sor][aktualis_oszlop+1])

        tiltott_helyek.append(rejtveny_terulet[aktualis_sor+1][aktualis_oszlop-1])
        tiltott_helyek.append(rejtveny_terulet[aktualis_sor+1][aktualis_oszlop])
        tiltott_helyek.append(rejtveny_terulet[aktualis_sor+1][aktualis_oszlop+1])

        print('---------------')

        tiltott_helyek = []

        for i in range(sor-1, sor + 2):
            for j in range(oszlop-1, oszlop + 2):
                # if i != sor and j != oszlop:
                if i == sor and oszlop == j:
                    ...
                else:
                    print(f"{i}, {j}")

        # for item in tiltott_helyek:
        #     print(f"{item[0]}, {item[1]}")


def feladat_2(sor, oszlop, tiltott_helyek):
    for i in range(sor-1, sor+2):
        for j in range(oszlop-1, oszlop +2):
            # ha benne van a táblázatban
            if i>=1 and i<=10 and j>=1 and j<=10:
                # a vizsgált értéket ne írjuk ki, csak minden mást
                if not (sor == i and oszlop == j):
                    tiltott_helyek.append([i, j])
                    print(f"{i}, {j}")

def rejtveny_terulet_generalas_nem_kell():
    
    global rejtveny_terulet
    rejtveny_terulet = []

    # sor
    for i in range(1, 11):
        temp = []
        # oszlopokat
        for j in range(1, 11):
            temp.append((i, j))
        rejtveny_terulet.append(temp)


def feladat_3():
    global feladvany_data, megoldas_data, darabolt_megoldas

    feladvany_data = get_data_from_txt(feladvany_path).split('\n')
    megoldas_data = get_data_from_txt(megoldas_path).split('\n')

    temp = {}

    # temp[megoldas_data[1]] = list(megoldas_data[2:12])
    iteracio = megoldas_data.pop(0)
    
    for i in range(int(iteracio)):
        data_idx = (i*11 + 1)
        megoldasok = []
        for j in list(megoldas_data[data_idx:data_idx + 10]):
            megoldasok.append(j.split(' '))
            # megoldasok.append()
        temp[megoldas_data[i*11]] = megoldasok

    darabolt_feladvany = []

    # list comprehension
    # darabolt_feladvany2 = [item.split(' ') for item in feladvany_data ]
    # print(darabolt_feladvany2)

    for i, item in enumerate(feladvany_data):
        if len(item) == 0:
            continue
        for idx, j in enumerate(item.split(' ')):
            if j != '0':
                darabolt_feladvany.append([i, idx, j])
    
    hibas = []
    for key, value in temp.items():   
        for j in darabolt_feladvany:
            
            if value[j[0]][j[1]] != j[2]:
                hibas.append(key)
                break

    if len(hibas) != 0:
        for item in list(set(hibas)):
            print(item)
    else:
        print('Mindegyik megoldás erre a heti feladványra érkezett.')

    darabolt_megoldas = temp

def feladat_4():
    hibas_db = 0
    darabolt_megoldas.pop('Ildefonz')
    for value in darabolt_megoldas.values():
        darab = 0
        for i in value:
           darab += i.count('11')

        if darab != 12:
            hibas_db += 1

    print(f"{hibas_db} 'hibás' megoldás volt beküldve.")


def feladat_5():

    darabolt_megoldas    


# tiltott_terulet_fnc()
# rejtveny_terulet_generalas()
##############megoldások################
# feladat_1()
# feladat_2(sor, oszlop, [])
feladat_3()
feladat_4()


print(tiltott_helyek)