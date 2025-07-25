n = int(input())

c = 0
for x in range(1, n):
    c += x
    print(f"Previous number is {x - 1}", end=" ")
    print(f"Current number is {x}", end=" ")
    print(f"Sum is {c}")    