def number_to_list(n):
    lst = []
    while n:
        lst.append(n % 10)
        n //= 10
    lst.reverse()
    return(lst)
print(number_to_list(123))