def is_increasing(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                return False
    return True
print(is_increasing([1,2,3,4,5]))