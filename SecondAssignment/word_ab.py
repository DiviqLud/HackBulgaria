def is_an_bn(word):
    acount = 0
    bcount = 0
    for i in range(0, len(word)):
        if word[i] not in 'ab':
            return False
    help1 = word[:len(word)//2]
    for j in help1:
        if j not in 'a':
            return False
        else:
            acount += 1
    help2 = word[len(word)//2:]
    for i in help2:
        if i not in 'b':
            return False
        else:
            bcount += 1
    if acount == bcount:
        return True
    else:
        return False
print(is_an_bn(""))
#True
print(is_an_bn("rado"))
#False
print(is_an_bn("aaabb"))
#False
print(is_an_bn("aaabbb"))
#True
print(is_an_bn("aabbaabb"))
#False
print(is_an_bn("bbbaaa"))
#False
print(is_an_bn("aaaaabbbbb"))
#True
