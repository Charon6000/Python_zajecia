class Uczelnia:
    listastudentow = []
    def __init__(self, listastudentow:list) -> None:
        self.listastudentow = listastudentow
    
    def WyswieltOcenyKoncowe(self):
        listaocen = [0,0,0,0,0,0]
        for i in self.listastudentow:
            if i.ocena == 2.0:
                listaocen[0] += 1
            elif i.ocena == 3.0:
                listaocen[1] += 1
            elif i.ocena == 3.5:
                listaocen[2] += 1
            elif i.ocena == 4.0:
                listaocen[3] += 1
            elif i.ocena == 4.5:
                listaocen[4] += 1
            elif i.ocena == 5.0:
                listaocen[5] += 1
            end = False
            #while end == True:
            height = len(self.listastudentow)
            for i in range(height,0,-1):
                for symb in listaocen:
                    if symb >= i:
                        print(f"\x1b[1;37;37mU|", end="  ")
                    else:
                        print(f"\x1b[1;32;37m", end=" |  ")
                print("")
            print("2|  3| 3.5| 4| 4.5| 5 |")
            print("___________________")
                
            

class Student:
    listapoprawnychocen = [2.0,3.0,4.0,5.0,3.5,4.5]
    __listaocen = [2,3,4,2,3,5]
    __ocena = None
    def __init__(self, imie:str, nazwisko:str, numer_albumu:float) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_albumu = numer_albumu
        self.__ocena = None
        self.Obliczsrednia()
    
    def Obliczsrednia(self):
        self.srednia = 0
        for i in self.listaocen:
            self.srednia += i
        self.srednia = self.srednia / len(self.__listaocen)

    @property
    def ocena(self):
        return self.__ocena

    @ocena.getter
    def ocena(self):
        return self.__ocena
    @ocena.setter
    def ocena(self, ocena):
        if ocena in self.listapoprawnychocen:
            self.__ocena = ocena
        else:
            print("Zla ocena")
    
    @property
    def listaocen(self):
        return self.__listaocen
    
    @listaocen.getter
    def listaocen(self):
        return self.__listaocen
    
    def dodajocene(self, ocena):
        if ocena in self.listapoprawnychocen:
            self.listaocen.append(ocena)
        else:
            print("Zla ocena")
        self.Obliczsrednia()

listastudentow = [Student("Tadeusz", "Norek", 690789),Student("Tadeusz", "Norek", 690789),Student("Tadeusz", "Norek", 690789),Student("Tadeusz", "Norek", 690789),Student("Tadeusz", "Norek", 690789)]
listastudentow[0].ocena = 2
listastudentow[1].ocena = 3
listastudentow[2].ocena = 4
listastudentow[3].ocena = 4.5
listastudentow[4].ocena = 4
pg = Uczelnia(listastudentow)
pg.WyswieltOcenyKoncowe()