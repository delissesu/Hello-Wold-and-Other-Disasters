list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list3 = []

for i in list1:
    if i % 2 != 0:
        list3.append(i)

for j in list2:
    if j % 2 == 0:
        list3.append(j)

print(list3)