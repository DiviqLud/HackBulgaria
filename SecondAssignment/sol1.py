def count_words(arr):
    diction = {}
    count = 0
    for i in arr:
        diction[i] = arr.count(i)
    return diction

print(count_words(["python", "python", "python", "ruby"]))