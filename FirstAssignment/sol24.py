def iterations_of_nan_expand(expanded):
    if expanded.count("NaN") == 1:
        return(expanded.count("Not a"))
    else:
        return False
print(iterations_of_nan_expand("Not a Not a NaN"))