def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


def prime_factorization(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    newlist = []
    tup = ()
    for i in lst:
        if is_prime(i):
            newlist.append(i)
    #return (newlist)
    count = 0
    finallist = []
    tup = ()
    for i in range(0,len(newlist)):
        while n:
            if n % newlist[0] == 0:
                count += 1
            else:
                break
            tup = tup + (i, count)
            finallist.append(tup)
    return finallist
print(prime_factorization(15))
