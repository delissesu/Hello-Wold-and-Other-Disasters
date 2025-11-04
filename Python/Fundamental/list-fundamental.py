import sys

list_angka : list[int] = []

for i in range(10):
    list_angka.append(i)
    print(i, list_angka, len(list_angka), sys.getsizeof(list_angka))

lst = [1, 2]
print("len =", len(lst))
print(lst)
print("size (bytes) =", sys.getsizeof(lst))

lst.append(30)
print(lst)
print("size (bytes) =", sys.getsizeof(lst))


# Cek List Baru
array_nama : list[str | int] = ["Naura", "Delion", "Naveria", "Aditya"]
print("Awal: ", array_nama)
print("ID Array: ", id(array_nama))

for indeks, value in enumerate(array_nama):
    print(f"Array[{indeks}] : {value}, ID : {id(array_nama[indeks])}")

print("Ukuran kontainer (Bytes): ", sys.getsizeof(array_nama))

# Tambah elemen supaya list melakukan resizing
for n in range(5, 10):
    array_nama.append(n)
    
    print(f"Elemen yang ditambahkan [{n}]")
    print("Ukuran kontainer (Bytes): ", sys.getsizeof(array_nama))
    print(f"ID Array Sekarang: [{id(array_nama)}]")
    
    for indeks, value in enumerate(array_nama):
        print(f"Array[{indeks}] : {value}, ID : {id(array_nama[indeks])}")

print("ID Array Terakhir: ", id(array_nama))
print("Ukuran kontainer (Bytes): ", sys.getsizeof(array_nama))