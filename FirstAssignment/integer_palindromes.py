def is_int_palindrome(n):
    newword = str(n)
    neww = newword[::-1]
    if newword == neww:
        return True
    else:
        return False

print(is_int_palindrome(122321))
