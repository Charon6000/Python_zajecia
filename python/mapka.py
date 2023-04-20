import time
import abc
import ctypes

GetAsyncKeyState = ctypes.windll.user32.GetAsyncKeyState
VK_Left = GetAsyncKeyState(0x25)
VK_Right = GetAsyncKeyState(0x27)
VK_UP = GetAsyncKeyState(0x26)
VK_Down = GetAsyncKeyState(0x28)
listamap = [["D","O","D", "W",], ["D","D","T","W"], ["T","T","P","W"],["P","P","W","W"]]

class Drawable(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self, kolor, kolor_tla, symbol) -> None:
        self.kolor = kolor
        self.kolor_tla = kolor_tla
        self.symbol = symbol
    def rysuj(self):
        pass
class Vector3:
    def __init__(self,x:float,y:float,z:float = 0) -> None:
        self.x=x
        self.y=y
        self.z=z
    def __str__(self) -> str:
        stronk = f"x: {self.x} y: {self.y} z: {self.z}"
        return stronk
        
    def __add__(self, other):
        return Vector3(self.x + other.x,self.y + other.y,self.z + other.z)
    
    def __mul__(self, other):
        if type(other)==type(self):
            return Vector3(self.x * other.x,self.y * other.y,self.z * other.z)
        else:
            return Vector3(self.x * other,self.y * other,self.z * other)
    
    def __iadd__(self, other):
        if type(other) == type(self):
         self.x +=other.x
         self.y += other.y
         self.z += other.z
         return self
        else:
            return Vector3(self.x +other.x, self.y+ other.y, self.z+other.z)
    
class Postac(Drawable):
    def __init__(self,nazwa:str, symbol, predkosc:Vector3,polozenie:Vector3,max_pr:float,masa:float, mapa:list) -> None:
        kolor = 37
        kolor_tla = 41
        super().__init__(kolor, kolor_tla, symbol)
        self.nazwa = nazwa
        self.predkosc=predkosc
        self.polozenie=polozenie
        self.max_pr= max_pr
        self.masa=masa
        
    # def przenies(self,deltaTime:float, mapa:list):
    #     while True:
    #         if VK_Left & 0x8000:
    #             self.polozenie = Vector3()
    #         if VK_Right & 0x8000:
    #             print("ARROW Right")
    #         if VK_UP & 0x8000:
    #             print("ARROW UP")
    #         if VK_Down & 0x8000:
    #             print("ARROW Down")
    #         self.predkosc +=  1 * deltaTime
    #         self.polozenie +=  self.predkosc * deltaTime
    #         print(f"\x1b[1;32;49m {self.predkosc}]")
    #         mapa = Mapa(mapa)
    #         time.sleep(deltaTime)
    
    # def przenies(self,przyspieszenie:Vector3,deltaTime:float, mapa:list):
    #     while True:
    #         if VK_Left & 0x8000:
    #             print("ARROW LEFT")
    #         if VK_Right & 0x8000:
    #             print("ARROW Right")
    #         if VK_UP & 0x8000:
    #             print("ARROW UP")
    #         if VK_Down & 0x8000:
    #             print("ARROW Down")
    #         self.predkosc +=  przyspieszenie * deltaTime
    #         self.polozenie +=  self.predkosc * deltaTime
    #         print(f"\x1b[1;32;49m {self.predkosc}]")
    #         mapa = Mapa(mapa)
    #         time.sleep(deltaTime)
class Pole(Drawable):
    def __init__(self, kolor, kolor_tla, symbol, x, y) -> None:
        super().__init__(kolor, kolor_tla, symbol)
        self.__x = x
        self.__y = y
    def rysuj(self):
        print(f"\x1b[1;32;{self.kolor}m {self.symbol}", end="")

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = min(x,20)

    @x.getter
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = min(y,20)

    

class Drzewo(Pole):
    def __init__(self, x, y) -> None:
        super().__init__(91, 0, "¥", x, y)

class Woda(Pole):
    def __init__(self, x, y) -> None:
        self.symbol = "~"
        self.kolor = 34
        self.kolor_tla = 0
        super().__init__(self.kolor, self.kolor_tla, self.symbol, x, y)

class Piasek(Pole):
    def __init__(self, x, y) -> None:
        self.symbol = "."
        self.kolor = 33
        self.kolor_tla = 0
        super().__init__(self.kolor, self.kolor_tla, self.symbol, x, y)

class Trawa(Pole):
    def __init__(self,  x, y) -> None:
        self.symbol = ","
        self.kolor = 32
        self.kolor_tla = 0
        super().__init__(self.kolor, self.kolor_tla, self.symbol, x, y)


class Mapa:
    def szerWys(self):
        self.szerokosc = len(self.listazmapa)
        self.wysokosc = len(self.listazmapa[0])
    
    def rysuj(self):
        self.konwertuj()
        # listamap[0][0].x = 30
        # print(listamap[0][0].x)
        for wiersz in self.listazmapa:
            print("\n", end="")
            for pole in wiersz:
                print(f"\x1b[1;32;{pole.kolor}m {pole.symbol}", end="")
    
    def konwertuj(self):
        for wiersz in range(0, len(self.listazmapa)):
            for pole in range(0, len(self.listazmapa[wiersz])):
                if self.listazmapa[wiersz][pole] == "D":
                    self.listazmapa[wiersz][pole] = Drzewo(wiersz, pole)
                elif self.listazmapa[wiersz][pole] == "T":
                    self.listazmapa[wiersz][pole] = Trawa(wiersz, pole)
                elif self.listazmapa[wiersz][pole] == "W":
                    self.listazmapa[wiersz][pole] = Woda(wiersz, pole)
                elif self.listazmapa[wiersz][pole] == "P":
                    self.listazmapa[wiersz][pole] = Piasek(wiersz, pole)
                elif self.listazmapa[wiersz][pole] == "O":
                    self.listazmapa[wiersz][pole] = Postac( "Skurwibonk","V", Vector3(0,0),Vector3(wiersz, pole),10, 5)
        
    def __init__(self, listazmapa):
        self.listazmapa = listazmapa
        self.szerWys()
        self.rysuj()