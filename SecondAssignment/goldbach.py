def is_prime(n):
    if(n == 1):
        return False
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True


def goldbach(n):
    primeNumbers = []
    goldbachResult = []
    for prime in range(1, n):
        if is_prime(prime):
            primeNumbers.append(prime)

    for el in range(0, len(primeNumbers)):
        for nextEl in range(el, len(primeNumbers)):
            if primeNumbers[el] + primeNumbers[nextEl] == n:
                tup = (primeNumbers[el], primeNumbers[nextEl])
                goldbachResult.append(tup)
    return goldbachResult

print(goldbach(100))
