class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambahKecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def kecepatanTurbo(self):
        self.kecepatan += 50

mobil_satu = Mobil("Putih", "Hyundai", 160)
print(mobil_satu.kecepatan)

mobil_sport = MobilSport("Merah", "Hyundai", 160)
print(mobil_sport.kecepatan)
mobil_sport.kecepatanTurbo()
print(mobil_sport.kecepatan)