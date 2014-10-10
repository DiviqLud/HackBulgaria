def sevens_in_a_row(arr, n):
    for i in range(0, len(arr)):
        if arr[i] == 7:
            count = 0
            if i + n < len(arr):
                for j in range(i, i + n):
                    if arr[j] == 7:
                        count += 1
                        print(count)
                    if count == n:
                        return True
    return False
print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 2))
