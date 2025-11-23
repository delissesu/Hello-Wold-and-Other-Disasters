MENU_MINUMAN = {
    "aqua" : {
        "harga": 15000,
        "stok" : 5
    },
    "sprite" : {
        "harga" : 5000,
        "stok" : 5
    },
    "chi forest" : {
        "harga" : 10000,
        "stok" : 7
    },
    "ultra milk" : {
        "harga" : 7000,
        "stok" : 3
    }
}

data_pelanggan = {
    "nama" : ""
}

keranjang_belanja = {}

welcome_text = "SELAMAT DATANG DI NAVERIA WATERY STORE!"
print("-" * len(welcome_text))
print(welcome_text)
print("-" * len(welcome_text))

print("\nREGISTRASI PELANGGAN")
data_pelanggan["nama"] = input("Masukkan Nama Kamu: ").title().strip()
print(f"SELAMAT DATANG {data_pelanggan['nama'].upper()}!")


print("-" * len(welcome_text))
print("MENU MINUMAN!")
print("-" * len(welcome_text))

menu_per_item = {}
for menu, item in MENU_MINUMAN.items():
    harga = item['harga']
    
    if harga not in menu_per_item:
        menu_per_item[harga] = []
    menu_per_item[harga].append(menu)

print(menu_per_item)