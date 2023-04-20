import math
class Punkt:
    x:int
    y:int

    def __init__(self,x,y):
        self.x = x
        self.y=y

    def __str__(self):
       strunk = f"x: {self.x} y: {self.y}"
       return strunk

class Odcinek:
    odc1:Punkt
    odc2:Punkt

    def __init__(self, odc1:Punkt, odc2:Punkt):
        self.odc1=odc1
        self.odc2=odc2

    def __str__(self):
        strunk = f"pkt1: {self.odc1} pkt2: {self.odc2}"
        return strunk
    def dlugosc(self):
        x = self.odc1.x - self.odc2.x
        y = self.odc1.y - self.odc2.y
        return math.sqrt(x**2 + y**2)

class Lamana:
    odc:list[Odcinek]

    def __init__(self, odc:list[Odcinek]):
        self.odc = odc
        
    def __str__(self) -> str:
        strunk = ""
        for c in self.odc:
            strunk += f"{c}\n"
        return strunk
    def dlugosc(self):
        dl = 0
        for c in self.odc:
            dl += c.dlugosc()
        return dl

pkt1=Punkt(2,3)
pkt2=Punkt(5,-1)
odc1 = Odcinek(pkt1,pkt2)
pkt1=Punkt(7,4)
pkt2=Punkt(5,-1)
odc2 = Odcinek(pkt2,pkt1)
odc = [odc1,odc2]
lamana = Lamana(odc)
print(lamana)