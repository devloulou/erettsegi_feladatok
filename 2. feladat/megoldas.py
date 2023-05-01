# indentáció
# Globális változó

file_name = r'C:\WORK\Peti_erettsegi\1. alkalom\2. feladat\adatok\konnyu.txt'
sorszam = 2
oszlop = 9

data = None
resztablazat = None


def feladat_1():
    global file_name, sorszam, oszlop

    file_name = input("Adja meg a bemeneti fájl nevét! ")
    sorszam = int(input("Adja meg egy sor számát!"))
    oszlop = int(input("Adja meg egy oszlop számát!"))

"""
def feladat_1():
    file_name = input("Adja meg a bemeneti fájl nevét! ")
    sorszam = int(input("Adja meg egy sor számát!"))
    oszlop = int(input("Adja meg egy oszlop számát!"))

    return file_name, sorszam, oszlop


file_name, sorszam, oszlop = feladat_1()
"""

# feladat_1()

def feladat_2():
    # global data
    with open(file_name, "r") as f:
        data = f.read().split('\n')

    return data



def feladat_3():

    lekert_ertek = data[sorszam-1].replace(' ', '')[oszlop-1]
    if int(lekert_ertek) == 0:
        print("„Az adott helyet még nem töltötték ki.”")
    else:
        print(f"Az adott helyen szereplő szám: {lekert_ertek}")
   

    if (sorszam /3) <= 1 and (oszlop / 3) <= 1:
        print("A hely a(z) 1 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 1 and (oszlop / 3) > 1 and (oszlop / 3) <= 2:
        print("A hely a(z) 2 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 1 and (oszlop / 3) > 2 and (oszlop / 3) <= 3:
        print("A hely a(z) 3 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 2 and (oszlop / 3) <= 1:
        print("A hely a(z) 4 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 2 and (oszlop / 3) > 1 and (oszlop / 3) <= 2:
        print("A hely a(z) 5 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 2 and (oszlop / 3) > 2 and (oszlop / 3) <= 3:
        print("A hely a(z) 6 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 3 and (oszlop / 3) <= 1:
        print("A hely a(z) 7 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 3 and (oszlop / 3) > 1 and (oszlop / 3) <= 2:
        print("A hely a(z) 8 résztáblázathoz tartozik.")
    elif (sorszam /3) <= 3 and (oszlop / 3) > 2 and (oszlop / 3) <= 3:
        print("A hely a(z) 9 résztáblázathoz tartozik.")
   

def feladat_4():
    cnt = 0
    for item in data[0:9]:
        temp = item.replace(' ', '')
        cnt += temp.count('0')

    szazelek = round(cnt/81*100, 1)
    
    print(f"Az üres helyek aránya: {szazelek} %")


def feladat_5():
    lepesek = data[9:-1]
    sudoku = data[0:9]

    for item in lepesek:
        sor = item.split(' ')
        sorszam = int(sor[1])
        oszlop = int(sor[2])
        szam = int(sor[0])

        print(f"A kiválasztott sor: {sorszam} oszlop: {oszlop} a szám: {szam} ")
        
        vizsgalt_szam = int(sudoku[sorszam-1].split(' ')[oszlop -1])
       
        if vizsgalt_szam != 0:
            print("A helyet már kitöltötték. ")
        
        else:
            # meg kell nézni az összes oszlopban szereple e
            # sorszám: megnézni, hogy a szam változó a sorban szerepel e
            
            # print(str(szam) in sudoku[sorszam-1])

            # sor vizsgálat
            sor_siker = False
            oszlop_siker = False
            resztablazat_siker = False

            if sudoku[sorszam-1].count(str(szam)) > 0:
                print("Az adott sorban már szerepel a szám")
                sor_siker = False
                continue
            else:
                sor_siker = True
            
            # oszlop vizsgálat
            for i in sudoku:
                temp = i.replace(' ', '')
                oszlop_siker = True
                # print(temp[oszlop-1] == szam)
                if int(temp[oszlop-1]) == szam:
                    print("Az adott oszlopban már szerepel a szám")
                    oszlop_siker = False
                    break
            
            if not oszlop_siker:
                continue
            # résztáblázat - le kellene gyűjteni külön listákba, a résztáblázatokat
            melyik_resz = get_reszhalmaz(sorszam, oszlop)
            
            if szam in resztablazat[melyik_resz-1]:
                print("Az adott résztáblázatban már szerepel a szám")
                resztablazat_siker = False
                continue
            else:
                resztablazat_siker = True

            if sor_siker == True and oszlop_siker == True and resztablazat_siker == True:
                print("A lépés megtehető")

def get_reszhalmaz(sor, oszlop):
    melyik_resz = None
    if sor/3 <= 1:
        resz_szam = 0
    elif sor/3 <= 2:
        resz_szam = 3
    else:
        resz_szam = 6

    if (oszlop/3) <= 1:
        melyik_resz = resz_szam + 1
    elif oszlop/3 <= 2:
        melyik_resz = resz_szam + 2
    elif oszlop/3 <= 3:
        melyik_resz = resz_szam + 3

    return melyik_resz


def generate_resztablazat():
    # [[5, 8, 2, 3, 7, 6, 9, 4, 1], []]
    resztablazat = [[], [], [], [], [], [], [], [], []]
    for idx, item in enumerate(data[0:9]):
        sor = item.replace(' ', '')      

        if idx/3 < 1:
            resz_szam = 0
        elif idx/3 < 2:
            resz_szam = 3
        else:
            resz_szam = 6

        for j_idx, j in enumerate(sor):
            if (j_idx/3) < 1:
                resztablazat[resz_szam].append(int(j))
            elif j_idx/3 < 2:
                resztablazat[resz_szam +1].append(int(j))
            elif j_idx/3 <= 3:
                resztablazat[resz_szam +2].append(int(j))
            
    return resztablazat
    
        


data = feladat_2()
resztablazat = generate_resztablazat()

teszt = get_reszhalmaz(4, 7)

feladat_3()
feladat_4()
feladat_5()