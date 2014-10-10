def count_consonants(str):
    count = 0
    for i in str:
        if i.lower() in "bcdfghjklmnpqrstvwxz":
            count += 1
    return count
print(count_consonants("Theistareykjarbunga"))