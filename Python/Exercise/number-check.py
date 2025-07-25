num_list = list(map(int, input().split()))
print(num_list)

first_num = num_list[0]
last_num = num_list[-1]

if first_num == last_num:
    print(True)
else:
    print(False)