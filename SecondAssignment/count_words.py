def count_words(arr):
    diction = {}
    for i in arr:
        diction[i] = arr.count(i)
    return diction

