MENU_MAKANAN = {
    "pizza": {
        "harga": 3.00,
        "kategori": "main course",
        "stok": 15,
        "kalori": 285,
        "deskripsi": "Pizza Italia dengan keju mozarella"
    },
    "burger": {
        "harga": 2.00,
        "kategori": "main course", 
        "stok": 20,
        "kalori": 540,
        "deskripsi": "Burger daging sapi dengan sayuran segar"
    },
    "fried rice": {
        "harga": 1.50,
        "kategori": "main course",
        "stok": 25,
        "kalori": 220,
        "deskripsi": "Nasi goreng spesial dengan telur dan sayuran"
    },
    "sandwich": {
        "harga": 5.00,
        "kategori": "main course",
        "stok": 10,
        "kalori": 300,
        "deskripsi": "Sandwich premium dengan daging asap"
    },
    "bread": {
        "harga": 1.00,
        "kategori": "snack",
        "stok": 30,
        "kalori": 80,
        "deskripsi": "Roti tawar segar"
    },
    "coffee": {
        "harga": 2.50,
        "kategori": "drink",
        "stok": 50,
        "kalori": 5,
        "deskripsi": "Kopi arabica premium"
    },
    "orange juice": {
        "harga": 1.75,
        "kategori": "drink", 
        "stok": 40,
        "kalori": 110,
        "deskripsi": "Jus jeruk segar 100% alami"
    }
}

data_pelanggan = {
    "nama": "",
    "email": "",
    "poin": 0
}

keranjang_belanja = {}

statistik_toko = {
    "total_transaksi": 0,
    "total_pendapatan": 0.0,
    "item_terlaris": "",
    "penjualan_per_kategori": {
        "main course": 0,
        "snack": 0,
        "drink": 0
    }
}

print("=" * 60)
print("SELAMAT DATANG DI ADVANCED DICTIONARY SHOP!")
print("=" * 60)

print("\nREGISTRASI PELANGGAN")
data_pelanggan["nama"] = input("Masukkan nama Anda: ").title()
data_pelanggan["email"] = input("Masukkan email Anda: ").lower()
data_pelanggan["poin"] = 100  # Poin welcome bonus

print(f"\nSelamat datang {data_pelanggan['nama']}!")
print(f"Anda mendapat 100 poin welcome bonus!")

def tampilkan_menu():
    print("\n" + "=" * 60)
    print("MENU MAKANAN & MINUMAN")
    print("=" * 60)
    
    # Group by kategori
    menu_per_kategori = {}
    for nama_makanan, detail in MENU_MAKANAN.items():
        kategori = detail["kategori"]
        if kategori not in menu_per_kategori:
            menu_per_kategori[kategori] = []
        menu_per_kategori[kategori].append(nama_makanan)
    
    nomor = 1
    for kategori, daftar_makanan in menu_per_kategori.items():
        print(f"\n{kategori.upper()}")
        print("-" * 40)
        for makanan in daftar_makanan:
            detail = MENU_MAKANAN[makanan]
            print(f"{nomor}. {makanan.title():<15} ${detail['harga']:.2f}")
            print(f"    Stok: {detail['stok']:<3} | {detail['kalori']} kal")
            print(f"    {detail['deskripsi']}")
            print()
            nomor += 1

tampilkan_menu()

print("\nMULAI BELANJA")
print("Ketik nama makanan untuk menambah ke keranjang")
print("Ketik 'menu' untuk melihat menu lagi")
print("Ketik 'keranjang' untuk melihat keranjang")
print("Ketik 'selesai' untuk checkout")

sedang_berbelanja = True
while sedang_berbelanja:
    perintah = input("\nApa yang ingin Anda lakukan? ").lower().strip()
    
    if perintah == "selesai":
        break
    elif perintah == "menu":
        tampilkan_menu()
    elif perintah == "keranjang":
        if not keranjang_belanja:
            print("Keranjang Anda masih kosong!")
        else:
            print("\n" + "=" * 40)
            print("ISI KERANJANG ANDA")
            print("=" * 40)
            total_harga = 0
            total_kalori = 0
            for item, info in keranjang_belanja.items():
                harga_item = info["harga"] * info["jumlah"]
                kalori_item = info["kalori"] * info["jumlah"]
                total_harga += harga_item
                total_kalori += kalori_item
                print(f"{item.title()}")
                print(f"    Jumlah: {info['jumlah']} | @${info['harga']:.2f} = ${harga_item:.2f}")
                print(f"    Kalori: {kalori_item} kal")
                print()
            print(f"Total Harga: ${total_harga:.2f}")
            print(f"Total Kalori: {total_kalori} kal")
    
    elif perintah in MENU_MAKANAN:
        # Cek stok
        if MENU_MAKANAN[perintah]["stok"] <= 0:
            print(f"Maaf, {perintah} sedang habis!")
            continue
            
        # Input jumlah
        try:
            jumlah = int(input(f"Berapa {perintah} yang ingin Anda beli? "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            elif jumlah > MENU_MAKANAN[perintah]["stok"]:
                print(f"Stok tidak cukup! Tersedia: {MENU_MAKANAN[perintah]['stok']}")
                continue
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        
        # Tambah ke keranjang
        if perintah in keranjang_belanja:
            keranjang_belanja[perintah]["jumlah"] += jumlah
        else:
            keranjang_belanja[perintah] = {
                "jumlah": jumlah,
                "harga": MENU_MAKANAN[perintah]["harga"],
                "kalori": MENU_MAKANAN[perintah]["kalori"],
                "kategori": MENU_MAKANAN[perintah]["kategori"]
            }
        
        # Update stok
        MENU_MAKANAN[perintah]["stok"] -= jumlah
        
        print(f"{jumlah} {perintah} berhasil ditambahkan ke keranjang!")
        
    else:
        print("Perintah tidak dikenali!")
        print("Coba ketik nama makanan, 'menu', 'keranjang', atau 'selesai'")

if keranjang_belanja:
    print("\n" + "=" * 60)
    print("CHECKOUT & RINGKASAN BELANJA")
    print("=" * 60)
    
    total_harga = 0
    total_kalori = 0
    total_item = 0
    
    print(f"Pelanggan: {data_pelanggan['nama']}")
    print(f"Email: {data_pelanggan['email']}")
    print("\nDetail Pembelian:")
    print("-" * 50)
    
    for item, info in keranjang_belanja.items():
        harga_item = info["harga"] * info["jumlah"]
        kalori_item = info["kalori"] * info["jumlah"]
        total_harga += harga_item
        total_kalori += kalori_item
        total_item += info["jumlah"]
        
        print(f"{item.title()}")
        print(f"    {info['jumlah']} x ${info['harga']:.2f} = ${harga_item:.2f}")
        print(f"    Kalori: {kalori_item} kal | Kategori: {info['kategori']}")
        print()
        
        statistik_toko["penjualan_per_kategori"][info["kategori"]] += info["jumlah"]
    
    diskon = 0
    if data_pelanggan["poin"] >= 50:
        diskon = total_harga * 0.1  # 10% diskon
        data_pelanggan["poin"] -= 50
        print(f"Diskon 10% (50 poin): -${diskon:.2f}")
    
    harga_akhir = total_harga - diskon
    poin_baru = int(harga_akhir)  # 1 dollar = 1 poin
    data_pelanggan["poin"] += poin_baru
    
    print("=" * 50)
    print(f"Subtotal: ${total_harga:.2f}")
    if diskon > 0:
        print(f"Diskon: -${diskon:.2f}")
    print(f"Total Pembayaran: ${harga_akhir:.2f}")
    print(f"Total Kalori: {total_kalori} kal")
    print(f"Poin Anda: {data_pelanggan['poin']} (+{poin_baru} dari pembelian ini)")
    
    # Update statistik toko
    statistik_toko["total_transaksi"] += 1
    statistik_toko["total_pendapatan"] += harga_akhir
    
    # Cari item terlaris berdasarkan keranjang
    item_terbanyak = max(keranjang_belanja.items(), key=lambda x: x[1]["jumlah"])
    statistik_toko["item_terlaris"] = item_terbanyak[0]
    
    print("\n" + "=" * 60)
    print("STATISTIK TOKO HARI INI")
    print("=" * 60)
    print(f"Total Transaksi: {statistik_toko['total_transaksi']}")
    print(f"Total Pendapatan: ${statistik_toko['total_pendapatan']:.2f}")
    print(f"Item Terlaris: {statistik_toko['item_terlaris'].title()}")
    print("\nPenjualan per Kategori:")
    for kategori, jumlah in statistik_toko["penjualan_per_kategori"].items():
        if jumlah > 0:
            print(f"   {kategori.title()}: {jumlah} item")
    
else:
    print("\nAnda belum membeli apapun. Terima kasih sudah berkunjung!")

print(f"\nTerima kasih {data_pelanggan['nama']}! Sampai jumpa lagi!")