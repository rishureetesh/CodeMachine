#Top Down
def LCSMTopDown(X, Y, n, m):
    table = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1];
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    
    i,j = n,m
    lcs = "";
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs += X[i - 1]
            i,j =i-1,j-1
        else:
            if table[i][j - 1] > table[i - 1][j]:
                j -= 1
            else:
                i -= 1
    
    lcs=lcs[::-1]
    return lcs
	


data = LCSMTopDown("abecd", "abyfc",5,5)
print(data)