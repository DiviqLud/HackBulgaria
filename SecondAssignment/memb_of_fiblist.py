def member_of_nth_fib_lists(listA, listB, needle):
    concatOfTwoList = []
    for elementInA in range(0, len(listA)):
        concatOfTwoList.append(listA[elementInA])
    for elementInB in range(0, len(listB)):
        concatOfTwoList.append(listB[elementInB])
    #return concatOfTwoList
    newNeedle = []
    for elNeedle in range(0, len(needle) + len(concatOfTwoList) - len(needle)):
        newNeedle.append(needle[elNeedle])
    if concatOfTwoList == newNeedle:
        return True
    else:
        return False


