# Basic while loop. if its true, go loop
ctr : int = 1
while ctr:
    print("Looking for someone else.")
    ctr -= 1

# Practice : i try to swap element in list to another list
num = range(10)
rl : list[int] = list(num)
nl_updater : list[int] = []
while rl:
    updater : int = rl.pop()
    nl_updater.append(updater)
for num in nl_updater: num += 1;print(num)

# Practice 2 : i try to sum all num in case the element can divide by 2
lnum : list[int] = [(num * 2) for num in range(100)]
ctr_num : list[int] = []
not_num : list[int] = [0 for _ in range(100)]
for num in lnum:
    if num % 2 == 0 and num is not 0:
        ctr_num.append(num)
    else:
        not_num.append(num)

new_num = sum(num for num in ctr_num if num > 100);print(new_num)
not_num.extend([num for num in ctr_num if num <= 100])
not_num = [num for num in not_num if num != 0];print(sum(not_num))