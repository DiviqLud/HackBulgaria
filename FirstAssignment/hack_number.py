def next_hack(number):
    n = number
    n += 1
    flag = True #This flag is only to capture the case
    while flag: #when number is 0
        intn = n
        binn = str(bin(intn))[2:]
        newn = binn[::-1]
        count = 0
        for i in binn:
            if i == '1':
                count += 1
        if binn == newn and count % 2 != 0:
            return(n)
        else:
            n += 1


print(next_hack(0))
