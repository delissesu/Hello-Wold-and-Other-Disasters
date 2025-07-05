# Parameter ini bebas, bisa diatur sesuka hati di argumen
def namaPanjang(nama_depan : str, nama_tengah : str, nama_belakang : str) -> str:
    return f"{nama_depan} {nama_tengah} {nama_belakang}"
print(namaPanjang(nama_depan="Aditya",nama_tengah= "Dwi", nama_belakang="Ferdiansyah"))
print(namaPanjang(nama_depan="Aditya",nama_tengah= "Ferdiansyah",nama_belakang= "Dwi"))

# Sama, tapi pakai integer
def angkaRandom(angka_satu : int, angka_dua : int) -> int:
    return angka_satu + angka_dua
print(angkaRandom(angka_dua=1, angka_satu=2))
print(angkaRandom(angka_satu=1, angka_dua=2))

# Contoh lebih jelas
def namAge(nama : str, umur : int) -> str:
    return f"{nama} berumur {umur} tahun"
print(namAge(nama="Delion", umur=21)) # Contoh 1
print(namAge(umur=21, nama="Delion")) # Contoh 2