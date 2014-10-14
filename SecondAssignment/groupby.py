def groupby(func, seq):
    result = {}
    for item in seq:
        result.setdefault(func(item), []).append(item)
    return result

print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))