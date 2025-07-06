class Manusia():
    def __init__(self, nama : str, umur : int, tinggi : int):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi

    def tambahTinggi(self):
        self.tinggi += 20

class ManusiaSuper(Manusia):
    def tambahTinggi(self): # Ini override
        self.tinggi += 30

    def kuranginTinggi(self):
        self.tinggi -= 10

manusia_biasa = Manusia("Aditya", 21, 186)

manusia_biasa.tambahTinggi()
print(manusia_biasa.tinggi)

manusia_super = ManusiaSuper("Delion", 20, 190)

manusia_super.tambahTinggi()
print(manusia_super.tinggi)

manusia_super.kuranginTinggi()
print(manusia_super.tinggi)