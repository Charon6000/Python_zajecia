import random
import math
class Wartosci:
    marki = ["🤍", "♦️", "♠️", "♣️"]
    wartosci = [1,2,3,4,5,6,7,8,9,10]

class Karty:
    marek:str
    wartosc:str
    def __init__(self, marek, wartosc) -> None:
        self.marek = marek
        self.wartosc = wartosc

class Talia(Wartosci):
    def __init__(self) -> None:
        super().__init__()
        self.tablica = []
        for m in self.marki:
            for w in self.wartosci:
                self.tablica.append(Karty(m,w))
    
    def Wypisz(self):
        for a in self.tablica:
            print(f"{a.marek} {a.wartosc}")
    
    def zdejmij_karte(self):
        if self.tablica != []:
            obiekt = self.tablica[len(self.tablica)-1]
            print(f"Zdjeto karte: {obiekt.marek} {obiekt.wartosc}")
            self.tablica.pop(len(self.tablica)-1)
        else:
            print("Nie ma żadnych kart w talii")
    
    def Tasuj(self):
        liczbyZrobione = []
        liczba = 0
        table = self.tablica.copy()
        for i in range(len(table)):
            item = table[i]
            while liczba in liczbyZrobione:
                liczba = random.randrange(len(self.tablica))
            liczbyZrobione.append(liczba)
            self.tablica[liczba] = item
        liczbyZrobione = []
        liczba = 0

t = Talia()
t.Tasuj()
gra1 = True
gra2 = True
tablica1 = []
tablica2 = []
while gra1 == True or gra2 == True:
    if gra1:
        tablica1.append(t.tablica[random.randrange(len(t.tablica))])
        print(f"Gracz 1: Dobrano karte {tablica1[len(tablica1)-1].marek} {tablica1[len(tablica1)-1].wartosc}")
        a = input("Czy gracz 1 chce pzrestac grac? T/N")
    
    if gra2:
        tablica2.append(t.tablica[random.randrange(len(t.tablica))])
        print(f"Gracz 2: Dobrano karte {tablica2[len(tablica2)-1].marek} {tablica2[len(tablica2)-1].wartosc}")
        b = input("Czy gracz 2 chce pzrestac grac? T/N")

    if a == "T":
        gra1 = True
    else:
        gra1 = False
    
    if b == "T":
        gra2 = True
    else:
        gra2 = False

suma1 = 0
suma2 = 0
for g1 in tablica1:
    suma1 += g1.wartosc

for g2 in tablica2:
    suma2 +=g2.wartosc

if abs(21-suma2)>abs(21-suma1):
   print("Wygrywa gracz 1")
elif abs(21-suma2) < abs(21-suma1):
   print("Wygrywa gracz 1")
else:
    print("Remis")
