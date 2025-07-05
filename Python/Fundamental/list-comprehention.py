# Is the basic list comprehention
lf : list[int] = [0 for _ in range(1, 10)]
print(lf)

# I try to make a list with random int
my_name : str = "Delissesu"
lo : list[int] = [(num ** 2) for num  in range(len((my_name))) if num != 0]
print(lo)

# Practice
int_matrix : list[list[int]] = [[] for _ in range(10)]
inp_nm : int = map(int, input().strip().split())
for num in inp_nm:
    int_matrix[num].append(num)
    print(int_matrix[num])
print(int_matrix)