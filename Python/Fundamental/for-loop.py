from typing import List

def sumRange(start: int, end: int) -> int:
    total: int = 0
    for i in range(start, end):
        total += i
    return total

def sumList(baris: int, kolom: int) -> List[int]:
    ttl_kolom : int = sum(range(kolom))
    return [ttl_kolom for _ in range(baris)]

# Basic for loop (1 inc, 9 exc)
df_num = sumRange(1, 10);print(df_num)

# Nested for loop logic encapsulated in a function
df_mx = sumList(10, 10);print(df_mx);print(*df_mx, sep="\n")