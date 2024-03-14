import timeit

AMOUNT_COINS = 998

# ЗАДАННЯ 1
def find_coins_greedy(amount):
    available_coins = [50, 25, 10, 5, 2, 1]
    coins_used = {}

    for coin in available_coins:
        coins_used[coin] = amount // coin
        amount = amount % coin
        if amount == 0:
            break

    return coins_used


print("Результат жадібного алгоритму:", find_coins_greedy(AMOUNT_COINS))


# ЗАДАННЯ 2
def find_min_coins(amount):
    available_coins = [1, 2, 5, 10, 20, 50]
    k = [[float(999)] * (amount + 1) for _ in range(len(available_coins))]

    for i in range(len(available_coins)):
        for j in range(amount + 1):
            if j == 0:
                k[i][j] = 0
            elif i == 0 or available_coins[i] > j:
                k[i][j] = k[i - 1][j]
            else:
                k[i][j] = min(k[i - 1][j], 1 + k[i][j - available_coins[i]])

    min_coins = k[-1][-1]
    used_coins = {}
    i = len(available_coins) - 1
    j = amount
    while min_coins > 0:
        if k[i - 1][j] == k[i][j]:
            i -= 1
        else:
            used_coins[available_coins[i]] = used_coins.get(available_coins[i], 0) + 1
            j -= available_coins[i]
            min_coins -= 1

    return used_coins


print(f"Результат динамічного алгоритму: {find_min_coins(AMOUNT_COINS)}")

greedy_time = timeit.timeit(lambda: find_coins_greedy(AMOUNT_COINS), number=1000)
dynamic_time = timeit.timeit(lambda: find_min_coins(AMOUNT_COINS), number=1000)

print(f"Час виконання жадібного алгоритму (усереднено по 1000 запусків): {greedy_time:.6f} сек. AMOUNT_SUM = {AMOUNT_COINS}")
print(f"Час виконання динамічного алгоритму (усереднено по 1000 запусків): {dynamic_time:.6f} сек. AMOUNT_SUM = {AMOUNT_COINS}")
