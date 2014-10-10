def contains_digit(number, digit):
    while number:
        if digit == number % 10:
            return True
        else:
            number //= 10
    else:
        return False

