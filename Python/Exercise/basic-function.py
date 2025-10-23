# def tes():
#     angka = [1, 2, 3, 4, 5]
#     p, l = 1, 2
#     hasil = p + l
#     angka.append(hasil)
#     return angka

# print(tes())
# operasi_lain = tes()

# hasil_baru = []
# for i in operasi_lain:
#     if i % 2 == 0:
#         hasil_baru.append(i)    

# total = sum(hasil_baru)
# print(total)
        
# def tes1():
#     angka = [1, 2, 3, 4, 5]
#     p, l = 1, 2
#     hasil = p + l
#     angka.append(hasil)
#     print(angka)

# tes1()
# print("ini")
# operasi_lain1 = tes1()
# print("coba dong", operasi_lain1)

# hasil_lain = []
# for i in operasi_lain1:
#     if i % 2 == 0:
#         hasil_lain.append(i)    

# total1 = sum(hasil_lain)
# print(total1)

"""
1. TAMBAH -> FUNGSI
2. KURANG -> FUNGSI
3. KALI -> FUNGSI
4. BAGI -> FUNGSI
"""
import os

def tambah(num1 : int, num2 : int) -> int:
    return num1 + num2 

def kurang(num1 : int, num2 : int) -> int:
    return num1 - num2 

def kali(num1 : int, num2 : int) -> int:
    return num1 * num2 

def bagi(num1 : int, num2 : int) -> float:
    return num1 / num2 

def pilihOperasi() -> str:
    pilih_operasi : str = input("Pilih operasi (1-5): ")
    return pilih_operasi

def clear() -> int:
    mati : int = os.system('cls' if os.name == 'nt' else 'clear')
    return mati
    
def main():
    mauNginput : bool = True
    while mauNginput:
        clear()
        print(
            "Kalkulator Sederhana\n"
            "1. Tambah\n"
            "2. Kurang\n"
            "3. Kali\n"
            "4. Bagi\n"
            "5. Keluar"
        )
        
        pilih_operasi = pilihOperasi()
        
        if pilih_operasi == "5":
            mauNginput = False
            clear()
            print("Terimakasih sudah menggunakan Kalkulator!")
            continue
        
        if pilih_operasi not in ["1", "2", "3", "4"]:
            print("Operasi yang kamu cari ga ada. Input ulang ya!")
            input("Tekan Enter untuk melanjutkan...")
            continue
        
        angka1 : int = int(input("Masukkan angka pertama: "))
        angka2 : int = int(input("Masukkan angka kedua: "))
        
        hasil = None  
            
        match pilih_operasi:
            case "1":
                hasil = tambah(angka1, angka2)
                print(f"Hasil penjumlahan dari angka {angka1} + angka {angka2} yaitu {hasil}")
            case "2":
                hasil = kurang(angka1, angka2)
                print(f"Hasil pengurangan dari angka {angka1} - angka {angka2} yaitu {hasil}")
            case "3":
                hasil = kali(angka1, angka2)
                print(f"Hasil perkalian dari angka {angka1} * angka {angka2} yaitu {hasil}")
            case "4":
                if angka2 == 0:
                    print("Gaboleh bagi dengan 0!")
                else:
                    hasil = bagi(angka1, angka2)
                    print(f"Hasil pembagian dari angka {angka1} / angka {angka2} yaitu {hasil}")
        
        input("\nTekan Enter untuk melanjutkan...")

main()