def unique_words_count(arr):
    diction = {}
    unique = 0
    for i in arr:
        diction[i] = arr.count(i)
    for key in diction:
        unique += 1
    return unique
print(unique_words_count(["HELLO!"] * 10))
