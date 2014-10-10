def biggest_difference(arr):
    a = max(arr)
    b = min(arr)
    return min(a - b, b - a)
print(biggest_difference([-10, -9, -1]))
