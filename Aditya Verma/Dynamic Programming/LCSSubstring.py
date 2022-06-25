#Top Down
def LCSMSubstring(X, Y, n, m):
    maxEle = -99999
    table = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1];
                maxEle = max(maxEle, table[i][j])
            else:
                table[i][j] = 0
    return maxEle


data = LCSMSubstring("abcdeecd", "abcdeyfc", 5, 5)
print(data)