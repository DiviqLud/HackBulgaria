def zero_insert(n):
    lst = []
    #zero = 0
    n = str(n)
    #count = 0
    for i in n:
        lst.append(int(i))
    for item in range(0,len(lst)*2):
        if lst[item] == lst[item+1] or ((lst[item] + lst[item+1]) % 10 == 0):
            lst.insert(item+1, 0)
    return lst
    
print(zero_insert(64646464))

#prevrushtam chisloto v list proverqvam dali elementite 
#otgovarqt na usloviqta i ako otgovarqt izpolzvame
# .append() sled tova vuv string zapisvame vseki element ot list-a ,
# castvame kum int i vrushtame rezultat
