# class Hero:
#     def __init__(self, nama, health):
#         self.nama = nama
#         self.health = health

#     def serang(self, hero_target):
#         hero_target.health -= 10

# class TampilkanHero:
#     def tampilkan(self, hero):
#         print(f"{hero.name} | HP: {hero.health}")

# class PenyimpanHero:
#     def simpan(self, hero, nama_file):
#         with open(nama_file, "a") as f:
#             f.write(f"{hero.name},{hero.health}\n")

# class Unit:
#     pass

# class UnitBergerak(Unit):
#     def bergerak(self):
#         pass

# class Minion(UnitBergerak):
#     def bergerak(self):
#         print("Minion sedang bergerak")

# class Lord(UnitBergerak):
#     def bergerak(self):
#         print("Lord sedang bergerak")

# def maju(unit):
#     unit.bergerak()

# maju(Minion())

# from abc import ABC, abstractmethod

# class BisaMenyerang(ABC):
#     @abstractmethod
#     def serang(self):
#         pass

# class BisaHeal(ABC):
#     @abstractmethod
#     def heal(self):
#         pass

# class Fighter(BisaMenyerang):
#     def serang(self):
#         print("Fighter menyerang")

# class Support(BisaMenyerang, BisaHeal):
#     def serang(self):
#         print("Support menyerang")

#     def heal(self):
#         print("Support memulihkan rekan")

# Fighter().serang()
# Support().heal()

from abc import ABC, abstractmethod

class Senjata(ABC):
    @abstractmethod
    def pukul(self):
        pass

class Pedang(Senjata):
    def pukul(self):
        return 20
    
class Panah(Senjata):
    def pukul(self):
        return 30

class Hero:
    def __init__(self, name, senjata):
        self.name = name
        self.senjata = senjata

    def serang(self):
        print(f"{self.name} menyerang dengan damage{self.senjata.pukul()}")

Hero("Balmond", Pedang()).serang()
Hero("Miya", Panah()).serang()