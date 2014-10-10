def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


def find_divisors(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return lst


def prime_factorization(n):
    newlist = []
    for i in find_divisors(n):
        if is_prime(i):
            newlist.append(i)
    #return (newlist)
    finallist = []
    count = 0
    for i in newlist:
        count = 0
        while n % i == 0:
                n /= i
                count += 1
        finallist.append(tuple([i, count]))
    return finallist
print(prime_factorization(10))
