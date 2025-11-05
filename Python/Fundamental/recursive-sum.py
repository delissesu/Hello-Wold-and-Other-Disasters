def sumRecursive(n):
    if n == 1: return 1
    else: return n + sumRecursive(n - 1)

print(sumRecursive(4))