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
    with open("1. alkalom/kerites.txt", "r") as f:
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

"""
4. Írjon a képernyőre egy házszámot a páratlan oldalról, amely melletti telken ugyanolyan
színű a kerítés! (A hiányzó és a festetlen kerítésnek nincs színe.) Feltételezheti, hogy van
ilyen telek, a több ilyen közül elég az egyik ház számát megjeleníteni. 
"""

# packing és unpacking

a, b = 10, 20

# unpacking művelet
a, b = [10, 20]
a, b = (10, 20)
# *b -> packing művelet
a, *b = [10, 20, 30]

# print(a, b)



def negyedik_feladat():
    temp = [] 
    for item in data: 
        sor = item.split(' ')

        if int(sor[0]) == 1:
            temp.append(sor)

    # mivel a temp-ben csak a páratlanok vannak
    # a lista indexei 0-tól indulnak
    # ha megvan az index értéke, akkor neküókn úgy kell majd számolnunk
    # figyelembe kell venni, hogy a pátarlan házszámok 1-el kezdődnek

    # enumerate függvény: enumerate(['Ricsi', 'Karcsi', 'Gabi']) -> [(0, 'Ricsi), (1, 'Karcsi'), (2, 'Gabi')]
    for idx, item in enumerate(temp):
        # print(item)
        # a színből replacelem a sortörést: a \n a sortörés karakter
        color = item[-1].replace('\n', '')

        if color in (':', '#'):
            continue

        if temp[idx+1][-1].replace('\n', '') == color:
            haz_szam = idx * 2 + 1
            print(f"A szomszédossal egyezik a kerítés színe: {haz_szam} ")
            break
        else:
            continue

def feladat_5():
    import string
    # hazszam = int(input(" addj meg egy házszámot \n"))

    hazszam = 83
    
    """
    a. Írja ki a házszámhoz tartozó kerítés színét, ha már elkészült és befestették,
    egyébként az állapotát a „#” vagy „:” karakter jelöli!
    """
    temp = []
    haz_idx = 0
    for item in data: 
        sor = item.split(' ')

        if hazszam % 2 == 0:
            if int(sor[0]) == 0:
                temp.append(sor)
                haz_idx = int(hazszam/2) -1
        else:
            if int(sor[0]) == 1:
                temp.append(sor)
                haz_idx = int((hazszam -1) / 2)

    color = temp[haz_idx][-1].replace('\n', '')
    print(temp[haz_idx])
    print(f"A kerítés színe / állapota: {color}")

    # ha a legelső számot adtuk meg, akkor csak 1 szomszédja van: utána lévő
    # ha az utolsó számot adtuk meg, akkor is csak 1 szomszédja: előtte lévő

    if haz_idx == 0:
        colors = []

        next_color = temp[haz_idx + 1][-1].replace('\n', '')
        colors.append(color)
        colors.append(next_color)

    elif haz_idx == len(temp)-1:
        colors = []

        prev_color = temp[haz_idx -1][-1].replace('\n', '')
        colors.append(color)
        colors.append(prev_color)

    else:
        colors = []

        colors.append(color)
        prev_color = temp[haz_idx -1][-1].replace('\n', '')
        next_color = temp[haz_idx + 1][-1].replace('\n', '')

        colors.append(prev_color)
        colors.append(next_color)

    print(colors)
    """
    A házszámhoz tartozó kerítést szeretné tulajdonosa be- vagy átfesteni. Olyan
színt akar választani, amely különbözik a mellette lévő szomszéd(ok)tól és a
jelenlegi színtől is. Adjon meg egy lehetséges színt! A színt a teljes palettából
(A–Z) szabadon választhatja meg.
    """
    alphabet = string.ascii_uppercase

    for item in alphabet:
        if item not in colors:
            print(f"Egy lehetséges festési szín: {item}")
            break

def feladat_6():
    temp = []

    for item in data: 
        sor = item.split(' ')

        if int(sor[0]) == 1:
            temp.append(sor)

    draw_color = ""
    house_numbers = ""
    for idx, item in enumerate(temp):
        color = item[-1].replace('\n', '')
        
        if idx == 0:
            val = 1
        else:
            val += 2

        draw_color += color*int(item[1])

        house_numbers += str(val) + " " *(int(item[1])-len(str(val)))


        # house_numbers += draw_color

    with open("utackep.txt", "w") as f:
        f.write(draw_color)
        f.write('\n')
        f.write(house_numbers)



data = beolvas()
feladat_1()
feladat_3()
negyedik_feladat()
feladat_5()
feladat_6()
# if __name__ == '__main__':
#     data = beolvas()

#     feladat_1()