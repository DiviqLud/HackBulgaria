def sum_matrix(arr):
    sum = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            sum += arr[i][j]
    return sum
print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
