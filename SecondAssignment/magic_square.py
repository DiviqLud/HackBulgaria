def check_rows(sum_of_first_row, matrix):
    for row in range(0, len(matrix)):
        #print(matrix[row])
        sum_of_current = 0
        for col in range(0, len(matrix)):
            sum_of_current += matrix[row][col]
        if sum_of_current == sum_of_first_row:
            return True
        else:
            return False


def check_cols(sum_of_first_row, matrix):
    for col in range(0, len(matrix)):
        sum_of_current = 0
        for row in range(0, len(matrix)):
            sum_of_current += matrix[row][col]
        if sum_of_current == sum_of_first_row:
            return True
        else:
            return False


def check_main_diagonal(sum_of_first_row, matrix):
    sum_of_current = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if row == col:
                sum_of_current += matrix[row][col]
    if sum_of_current == sum_of_first_row:
        return True
    else:
        return False


def check_second_diagonal(sum_of_first_row, matrix):
    sum_of_current = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if row == len(matrix) - col - 1:
                sum_of_current += matrix[row][col]
    if sum_of_current == sum_of_first_row:
        return True
    else:
        return False


def magic_square(matrix):
    result_list = []
    sum_of_first_row = 0
    #so we can check later if other rows are equal to the first one
    for element in matrix[0]:
        sum_of_first_row += element
    #return sum_of_first_row
    count = 0
    if check_rows(sum_of_first_row, matrix) is True:
        count += 1
    if check_cols(sum_of_first_row, matrix) is True:
        count += 1
    if check_main_diagonal(sum_of_first_row, matrix) is True:
        count += 1
    if check_second_diagonal(sum_of_first_row, matrix) is True:
        count += 1

    if count == 4:
        return True
    else:
        return False

print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
