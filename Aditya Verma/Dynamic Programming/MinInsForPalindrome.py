#Minimum insertion to make string palindrome
def LCS(X,Y,n,m):
    table = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i - 1] == Y[j - 1] and i != j:
                table[i][j] = 1 + table[i - 1][j - 1];
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n][m]

def LCP(X, n):
    return LCS(X, X[::-1], n, n)

def MinInsPalindrome(X, n):
    return n-LCP(X, n)

data = MinInsPalindrome("abcd", 4)
print(data)