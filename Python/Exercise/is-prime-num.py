number = int(input())
def isPrime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        else:
            return True

n = 20
primes = []
for i in range(2, n + 1):
    if isPrime(i):
        primes.append(i)

print(primes)