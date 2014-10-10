def is_number_balanced(n):
    numb = str(n)
    first_half_sum = 0
    second_half_sum = 0
    number1 = int(numb[0:len(numb)//2])
    number2 = int(numb[len(numb)//2:])
    while number1:
        first_half_sum += number1 % 10
        number1 //= 10
    print(first_half_sum)
    while number2:
        second_half_sum += number2 % 10
        number2 //= 10
    print(second_half_sum)
    if first_half_sum == second_half_sum:
        return True
    else:
        return False
print(is_number_balanced(4518))
