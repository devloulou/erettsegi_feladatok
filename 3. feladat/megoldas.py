"""
0 - víz
1-9 - világító torony
11 - hajó
"""


feladat_data = None
megoldas_data = None
feladvany_path = r""
megoldas_path = r""

sor = 2
oszlop = 3
ertek = 2
rejtveny_terulet = None



def get_data_from_txt():
    ...

def feladat_1():
    """
    be kell kérni az input fv-el a sor, oszlop és ertek adatokat
    """
    global sor, oszlop, ertek

    sor = int(input("Sor: "))
    oszlop = int(input("Oszlop: "))
    ertek = int(input("Ertek: "))

def feladat_2():
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

def rejtveny_terulet_generalas():
    
    global rejtveny_terulet
    rejtveny_terulet = []

    # sor
    for i in range(1, 11):
        temp = []
        # oszlopokat
        for j in range(1, 11):
            temp.append((i, j))
        rejtveny_terulet.append(temp)


# feladat_1()

rejtveny_terulet_generalas()
feladat_2()