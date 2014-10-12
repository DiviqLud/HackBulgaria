def magic_square(matrix):
    resultList = []
    sumOfFirstRow = 0
    #so we can check later if other rows are equal to the first one
    for element in matrix[0]:
        sumOfFirstRow += element
    #return sumOfFirstRow
    sumOfCurrent = 0
    for row in range(0, len(matrix)):
        #print(matrix[row])
        sumOfCurrent = 0
        for col in range(0, len(matrix)):
            sumOfCurrent += matrix[row][col]
        if sumOfCurrent == sumOfFirstRow:
            resultList.append(sumOfCurrent)
        else:
            return False

    for col in range(0, len(matrix)):
        sumOfCurrent = 0
        for row in range(0, len(matrix)):
            sumOfCurrent += matrix[row][col]
        if sumOfCurrent == sumOfFirstRow:
            resultList.append(sumOfCurrent)
        else:
            return False

    sumOfCurrent = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if row == col:
                sumOfCurrent += matrix[row][col]
    if sumOfCurrent == sumOfFirstRow:
        resultList.append(sumOfCurrent)
    else:
        return False

    sumOfCurrent = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if row == len(matrix) - col - 1:
                sumOfCurrent += matrix[row][col]
    if sumOfCurrent == sumOfFirstRow:
        resultList.append(sumOfCurrent)
    else:
        return False

    count = 0
    for element in resultList:
        if element == sumOfFirstRow:
            count += 1
        else:
            False
    if count == len(resultList):
        return True

print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))