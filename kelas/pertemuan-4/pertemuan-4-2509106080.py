# # class Animal:

# #     def __init__(self, nama, umur, warna_bulu, berbisa):
# #         self.nama = nama
# #         self.umur = umur
# #         self.warna_bulu = warna_bulu
# #         self.berbisa = berbisa

# # kucing = Animal("oren", 1, "oren", None)
# # ular_cobra = Animal("cobra", 2, None, True)

# class Animal:

#     def __init__(self, nama, umur, warna_bulu, berbisa):
#         self.nama = nama
#         self.umur = umur

# class Mamalia(Animal):

#     def __init__(self, nama, umur, warna_bulu):
#         super().__init__(nama, umur)
#         self.warna_bulu = warna_bulu

#     def

# class Reptil(Animal):

#     def __init__(self, berbisa):
#         self.berbisa = berbisa

# class karyawan:
#     def __init__(self, nama, nip):
#         self.nama = nama
#         self.nip = nip

# class Teller(Karyawan):
#     def __init__(self, nama, nip):
#         super().__init__(nama, nip, "Teller")
        
#     def layani_setoran(self, rekening, nominal):
# # Asosiasi: rekening diterima sebagai parameter method
#         print(f" Teller {self.nama} melayani setoran...")

# rekening.setor(nominal, f"Setoran via teller {self.nip}")