def simplify_fraction(fraction):
    irreducablelist = [0, 0]
    newlist = []
    minum = min(fraction)
    #print(minum)
    for i in range(1, minum+1):
        if minum % i == 0:
            newlist.append(i)
    for i in newlist:
        #print(i)
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            irreducablelist[0] = fraction[0] // i
            irreducablelist[1] = fraction[1] // i
    return irreducablelist

print(simplify_fraction((3, 9)))
#(1,3)
print(simplify_fraction((1, 7)))
#(1,7)
print(simplify_fraction((4, 10)))
#(2,5)
print(simplify_fraction((63, 462)))
#(3,22)
