#Top Down
def ShortestCommonSupersequence(X, Y, n, m):
    table = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1];
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    i,j = n,m
    scs = "";
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            scs += X[i - 1]
            i,j =i-1,j-1
        elif table[i][j-1] > table[i-1][j]:
            scs += Y[j-1]
            j -= 1
        else:
            scs += X[i-1]
            i -= 1
    
    while i>0:
        scs += X[i-1]
        i -= 1
    
    while j>0:
        scs += Y[j-1]
        j -= 1
    
    return scs[::-1]

data = ShortestCommonSupersequence("abecd", "abyfc",5,5)
print(data)