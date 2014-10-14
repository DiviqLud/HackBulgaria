def is_decreasing(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] < seq[j]:
                return False
    return True
print(is_decreasing([5, 4, 3, 2, 9]))