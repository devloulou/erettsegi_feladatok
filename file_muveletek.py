"""
File műveletek

1. meg kell nyitnod a filet:
    - mindig meg kell adnod a file elérési útvonalát
    - meg kell adnod, hogy milyen megnyitási formát akarsz
         - olvasásra: r
         - ha írásra: w
2. elvégzed a feladatot
3. mindig zárd le a filet, ha végeztél
"""


file_path = r'C:\WORK\Peti_erettsegi\1. alkalom\adatok\kerites.txt'

data = []

"""
Minden olyan változó, ami a 0. indentációs szinten van - a sor elején - 
akkor az globális változó - mert őt mindenki látja, eléri és tudja használni az értékét

egy függvénynek mindig van visszatérési értéke
függetlenül attól, hogy te rendelezel e róla
"""
def beolvas():

    temp = "Ricsi"
    with open("kerites.txt", "r") as f:
    # read() a file teljes tartalmát kiolvassa és egy stringként adja vissza
    #data = f.read().split('\n')
        data = f.readlines()
    return data


def feladat_1():
    print(f"Eladott telkek száma: {len(data)}")


# A páros oldalon adták el az utolsó telket.
# Az utolsó telek házszáma: 78 
def feladat_3():
    utolso_adat = data[-1]
    utolso_adat = data[len(data)-1]
    utolso_adat = utolso_adat.split(' ')
    paros_e = int(utolso_adat[0])

    paros_db = 0
    paratlan_db = 1
    for i in data:
        if i[0] == '0':
            paros_db += 2
        else: 
            paratlan_db += 2

    if paros_e == 0:
        print("A páros oldalon adták el az utolsó telket")
        print(f"Az utolsó telek házszáma:{paros_db} ")
    else:
        print("A páratlan oldalon adták el az utolsó telket")
        print(f"Az utolsó telek házszáma:{paratlan_db} ")

data = beolvas()
feladat_1()
feladat_3()

# if __name__ == '__main__':
#     data = beolvas()

#     feladat_1()