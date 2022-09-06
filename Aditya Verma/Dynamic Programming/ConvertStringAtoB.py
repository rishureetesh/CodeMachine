#Top Down
#Convert string a to b by minimum insertion or deletion
def ShortestCommonSupersequence(X, Y, n, m):
    table = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1];
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n][m]

def SCS(X, Y, n, m):
    lcs_len = ShortestCommonSupersequence(X, Y, n, m)
    print("Minimum number of deletions = ", n - lcs_len)
    print("Minimum number of insertions = ", m - lcs_len)


SCS("abecd", "abyfc",5,5)