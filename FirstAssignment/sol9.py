from sol8 import contains_digit
def contains_digits(number, digits):
    count = 0
    for digit in digits:
        if contains_digit(number, digit) == True:
            count += 1
    if count == len(digits):
        return True
    else:
        return False
print(contains_digits(124753, [1, 2, 3, 7]))
