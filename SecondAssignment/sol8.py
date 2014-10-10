def sort_fractions(fractions):
    #newlist = []
    #finallist = []
    print(fractions)
    for i in range(0, len(fractions)-1):
        for j in range(0, len(fractions[i])-1):
            if fractions[i][j] / fractions[i][j+1] > fractions[i+1][j] / fractions[i+1][j+1]:
                swap = fractions[i]
                fractions[i] = fractions[i+1]
                fractions[i+1] = swap
    return fractions
        
print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

