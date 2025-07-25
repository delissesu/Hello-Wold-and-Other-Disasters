num = int(input())
num_two = int(input())

for _ in range(10):
    print(num, end=" ")
    result = num + num_two
    num = num_two
    num_two = result