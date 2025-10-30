x = 10
y = x
print(id(x), id(y))  # sama

y += 1
print(id(x), id(y))  # beda sekarang

a = [1, 2, 3]
b = a
print("Awal:", id(a), id(b))   # sama
print(id(a[0]), id(a[1]), id(b[len(b)-1]), id(a[2]))

b.append(99)
print("Akhir:", id(a), id(b))  # tetap sama
print("A:", a)
print("B:", b)
