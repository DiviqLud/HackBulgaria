def calculate_coins(sum):
    coins = [100, 50, 20, 10, 5, 2, 1]
    sum *= 100
    fixsum = sum
    diction = {}

    for coin in coins:
        diction[coin] = 0

    count = 0
    for coin in coins:
        count = 0
        while fixsum > coin:
            sum = sum - coin
            count += 1
            diction[coin] = count
            fixsum = sum
    return diction

print(calculate_coins(8.94))
