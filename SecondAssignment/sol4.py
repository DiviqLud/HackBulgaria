def prepare_meal(number):
    string = ""
    count = 0
    for i in range(1, number):
        if number % 3**i == 0:
            count += 1
    if count != 0:
        string = string + count*"spam "
        if number % 5 == 0:
            string = string + "and eggs"
            return string
        else:
            return string
    else:
        if number % 5 == 0:
            string = string + "eggs"
            return string
        else:
            return ""
print(prepare_meal(5))
