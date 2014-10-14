def nan_expand(times):
    str1 = 'NaN'
    str2 = 'Not a '
    newstr = ''
    if times == 0:
        return ""
    else:
        for i in range(1,times+1):
            str1 = str2 + str1
    return(str1)
print(nan_expand(4))