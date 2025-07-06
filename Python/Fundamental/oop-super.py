class KelasInduk:
    def __init__(self) -> None:
        print("Inisiialisasi Kelas Induk")

    def metode(self) -> None:
        print("Metode Kelas Induk")

class KelasTurunan(KelasInduk):
    def __init__(self) -> None:
        super().__init__()
        print("Inisialisasi Kelas Turunan")

    def metode(self) -> None:
        super().metode()
        print("Metode Kelas Turunan")

objek = KelasTurunan()
objek.metode()

# Practice
class Mobil:
    def __init__(self, merek : str, warna : str, kecepatan : int) -> None:
        self.merek = merek
        self.warna = warna
        self.kecepatan = kecepatan

    def tambahKecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 20

    def tambahKecepatan(self):
        super().tambahKecepatan()
        print("Kecepatan mobil bertambah, hati-hati!")

# Kelas Mobil Sport
mobil_sport = MobilSport("Hyundai", "Hitam", 190)
mobil_sport.turbo()
mobil_sport.tambahKecepatan()
mobil_sport.turbo()
print(mobil_sport.kecepatan)

mobil_sport.tambahKecepatan()
print(mobil_sport.kecepatan)
