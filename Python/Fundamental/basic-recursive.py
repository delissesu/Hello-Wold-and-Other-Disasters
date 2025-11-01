def tambah(lst, n):
    if n == 0:              # base case
        return
    lst.append(n)           # ubah isi list (mutable)
    print("Frame n =", n,"id n", id(n), "| id(lst) =", id(lst), "| isi =", lst)
    tambah(lst, n-1)        # recursive call

a = []
tambah(a, 3)
print("Hasil akhir:", a)

def jumlah(n):
    if n == 0:               # base case
        return 0
    print("Frame n =", n, "| id(n) =", id(n))
    return n + jumlah(n-1)

print("Hasil:", jumlah(5))
