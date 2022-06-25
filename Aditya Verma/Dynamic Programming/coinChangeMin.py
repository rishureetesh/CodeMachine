INF = 999999;
def CoinChangeMin(coinList, sum, coins):
    table = [[0 for sum in range(sum+1)] for coin in range(coins+1)]
    for i in range(0, coins+1):
        for j in range(0, sum+1):
            if j == 0:
                table[i][j] = 0
            if i == 0:
                table[i][j] = INF
            if i == 1:
                if j % coinList[i - 1] == 0:
                    table[i][j] = j / coinList[i - 1]
                else:
                    table[i][j] = INF

    for i in range(1, coins+1):
        for j in range(1, sum+1):
            if coinList[i-1] <= j:
                table[i][j] = min(table[i-1][j],1+table[i][j-coinList[i-1]])
            else:
                table[i][j] = table[i-1][j]
    return table[coins][sum]


arr = [1, 2, 3]
print(CoinChangeMin(arr, 4, len(arr)))