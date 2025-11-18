# Variabel untuk menyimpan data belanja
daftar_barang = []      # List untuk menyimpan nama barang
total_harga = 0.0       # Total harga semua barang
maksimal_barang = 4     # Batas maksimal barang yang bisa dibeli

print("=== SELAMAT DATANG DI SIMPLE SHOPPING DISCOUNT ===")
print("Maksimal 4 item per transaksi")
print("Dapatkan diskon berdasarkan jumlah item yang dibeli!")
print("- 4 barang = diskon 20%")
print("- 3 barang = diskon 15%") 
print("- 2 barang = diskon 10%")
print("- 1 barang = tidak ada diskon\n")

# Loop untuk input barang (maksimal 4 barang)
while len(daftar_barang) < maksimal_barang:
    
    # Input nama barang dengan validasi
    while True:
        nama_barang = input("Masukkan nama item yang ingin kamu tambahkan: ").strip().lower()
        
        # Cek apakah input tidak kosong
        if nama_barang != "":
            daftar_barang.append(nama_barang)  # Tambahkan ke list
            break
        else:
            print("Barang yang diinput tidak boleh kosong!")
    
    # Input harga barang dengan validasi
    while True:
        try:
            harga_barang = float(input(f"Masukkan harga untuk {nama_barang} (USD): $"))
            
            # Cek apakah harga tidak negatif
            if harga_barang >= 0:
                total_harga = total_harga + harga_barang  # Tambahkan ke total
                break
            else:
                print("Harga tidak boleh negatif!")
                
        except ValueError:
            print("Harap masukkan angka yang valid!")
    
    # Tampilkan informasi item yang baru ditambahkan
    print(f"Item '{nama_barang}' dengan harga ${harga_barang:.2f} telah ditambahkan!")
    print(f"Total barang: {len(daftar_barang)}/{maksimal_barang}")
    print(f"Total harga sementara: ${total_harga:.2f}")
    print("-" * 50)
    
    # Cek berapa barang yang tersisa
    sisa_barang = maksimal_barang - len(daftar_barang)
    if sisa_barang == 1:
        print("Kamu memiliki 1 barang tersisa untuk diinput!")
    elif sisa_barang == 0:
        print("Ini adalah barang terakhir yang bisa diinput.")

# Setelah selesai input, tampilkan ringkasan belanja
print("\n" + "=" * 50)
print("RINGKASAN BELANJA".center(50))
print("=" * 50)

print("Daftar barang yang dibeli:")
for i in range(len(daftar_barang)):
    nomor = i + 1
    print(f"{nomor}. {daftar_barang[i].title()}")

print(f"\nTotal barang: {len(daftar_barang)} item")
print(f"Total harga sebelum diskon: ${total_harga:.2f}")

# Hitung diskon berdasarkan jumlah barang
jumlah_barang = len(daftar_barang)
persentase_diskon = 0.0

if jumlah_barang == 4:
    persentase_diskon = 0.20    # 20% diskon
elif jumlah_barang == 3:
    persentase_diskon = 0.15    # 15% diskon
elif jumlah_barang == 2:
    persentase_diskon = 0.10    # 10% diskon
else:
    persentase_diskon = 0.0     # Tidak ada diskon

# Hitung dan tampilkan hasil akhir
if persentase_diskon > 0:
    jumlah_diskon = total_harga * persentase_diskon
    harga_akhir = total_harga - jumlah_diskon
    
    print(f"Diskon ({persentase_diskon * 100:.0f}%): -${jumlah_diskon:.2f}")
    print(f"Total harga setelah diskon: ${harga_akhir:.2f}")
    print(f"Kamu hemat: ${jumlah_diskon:.2f}!")
else:
    print("Tidak ada diskon untuk pembelian 1 item.")
    print(f"Total yang harus dibayar: ${total_harga:.2f}")

print("\nTerima kasih telah berbelanja!")
        