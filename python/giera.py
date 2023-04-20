import time
class Drawable:
    def __init__(self, kolor, kolor_tla, symbol) -> None:
        pass
    def rysuj(self):
        pass
class Vector3:
    def __init__(self,x:float,y:float,z:float) -> None:
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
    
class Postac:
    def __init__(self,nazwa:str,predkosc:Vector3,polozenie:Vector3,max_pr:float,masa:float) -> None:
        self.nazwa = nazwa
        self.predkosc=predkosc
        self.polozenie=polozenie
        self.max_pr= max_pr
        self.masa=masa
        
    def przenies(self,przyspieszenie:Vector3,deltaTime:float):
        while True:
            self.predkosc +=  przyspieszenie * deltaTime
            self.polozenie +=  self.predkosc * deltaTime
            print(f"\x1b[1;32;49m {self.predkosc}]")
            time.sleep(deltaTime)
        
Kuba = Postac("Kuba", Vector3(1,0,0), Vector3(0,0,0), 10, 65)
Kuba.przenies(Vector3(0,1,2), .10)