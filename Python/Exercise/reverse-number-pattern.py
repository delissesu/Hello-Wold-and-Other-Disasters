number = int(input())

for i in range(1, number + 1):
    for j in range(number - i + 1):
        print(i, end=" ")
    print()