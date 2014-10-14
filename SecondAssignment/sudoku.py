def square_solved(matrix):
    count = 0
    sum = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if matrix[row][col] in range(1, 10):
                count += 1
    if count == 9:
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix)):
                sum += matrix[row][col]
    if sum == 45:
        return True
    else:
        return False


def help_function(rowstart, rowend, colstart, colend, sudoku):
    miniSquare = []
    for row in range(rowstart, rowend):
        help = []
        for col in range(colstart, colend):
            help.append(sudoku[row][col])
        miniSquare.append(help)
    return miniSquare


def sudoku_solved(sudoku):
    count = 0
    for row in range(0, len(sudoku)):
        for el in range(0, len(sudoku)):
            #print(sudoku[row][el])
            if sudoku[row][el] in range(1, 10):
                count += 1
    if count == 81:
        sum = 0
        resultCounter = 0
        for row in range(0, len(sudoku)):
            sum = 0
            for col in range(0, len(sudoku)):
                sum += sudoku[row][col]
            if sum == 45:
                resultCounter += 1
        for row in range(0, len(sudoku)):
            sum = 0
            for col in range(0, len(sudoku)):
                sum += sudoku[col][row]
            if sum == 45:
                resultCounter += 1

        firstLen = len(sudoku)//3
        secLen = len(sudoku)//3 + 3

        if help_function(0, firstLen, 0, firstLen, sudoku):
            resultCounter += 1
        if help_function(0, firstLen, firstLen, secLen, sudoku):
            resultCounter += 1
        if help_function(0, firstLen, secLen, len(sudoku), sudoku):
            resultCounter += 1
        if help_function(firstLen, secLen, 0, firstLen, sudoku):
            resultCounter += 1
        if help_function(firstLen, secLen, firstLen, secLen, sudoku):
            resultCounter += 1
        if help_function(firstLen, secLen, secLen, len(sudoku), sudoku):
            resultCounter += 1
        if help_function(secLen, len(sudoku), 0, firstLen, sudoku):
            resultCounter += 1
        if help_function(secLen, len(sudoku), firstLen, secLen, sudoku):
            resultCounter += 1
        if help_function(secLen, len(sudoku), secLen, len(sudoku), sudoku):
            resultCounter += 1
    else:
        return False
    if resultCounter == 27:
        return True
    else:
        return False
print(sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
