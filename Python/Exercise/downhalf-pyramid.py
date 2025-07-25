num = int(input())
for i in range(num, 0, -1):
    for j in range(0, i - 1):
        print(j, end=" ")
    print()