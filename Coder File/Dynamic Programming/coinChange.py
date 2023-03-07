def CoinChangeMax(coinList, sum, coins):
    table = [[0 for sum in range(sum+1)] for coin in range(coins+1)]
    for i in range(sum+1):
        table[0][i] = 1

    for i in range(1, coins+1):
        for j in range(1, sum+1):
            if coinList[i-1] <= j:
                table[i][j] = table[i-1][j]+table[i][j-coinList[i-1]]
            else:
                table[i][j] = table[i-1][j]
    return table[coins][sum]


arr = [1, 2, 3]
print(CoinChangeMax(arr, 4, len(arr)))
